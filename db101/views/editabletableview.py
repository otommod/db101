import tkinter as tk
from tkinter import ttk

from ..exceptions import ModelError
from ..models import NamedTable
from ..widgets import EditableMultiColumnList
from .errorview import ErrorView
from .singleselectiontableview import SingleSelectionTableView
from .tableview import TableView


class EditableTableView(TableView, EditableMultiColumnList):
    def __init__(self, parent, table):
        self.popup = None
        super().__init__(parent, table)

        self._tree.bind("<1>", self.__on_click, add="+")
        self._tree.bind("<3>", self.__on_right_click, add="+")
        self.cell_edited.add_observer(self.__on_changed)

        self.fill()

    def _get_key(self, item):
        return {k: self.set(item, k) for k in self.table.keyfields}

    def fill(self):
        self._destroy_popup_menu()
        super().fill()

    def create(self, new_item):
        try:
            self.table.append(new_item)
        except ModelError as e:
            ErrorView(e)

    def delete(self, keys):
        try:
            for k in keys:
                self.table.delete(k)
        except ModelError as e:
            ErrorView(e)

    def _create_popup_menu(self):
        popup = tk.Menu(self._tree, tearoff=False)
        selection = self._tree.selection()

        def delete():
            self.delete(self._get_key(item) for item in selection)

        def insert():
            win = tk.Toplevel()
            win.title("Inserting...")
            win_frame = ttk.Frame(win)
            win_frame.grid()

            entries = {}
            for i, c in enumerate(self.table.fields):
                print(c, self.table.fkeys)
                if c in self.table.fkeys:
                    reference = NamedTable.lookup(self.table.fkeys[c])
                    entry = SingleSelectionTableView(win, reference)
                    entry.grid(in_=win_frame, row=1, column=0, columnspan=2,
                               sticky="nsew")

                    # is this the worst code ever? possibly
                    class hide_get:
                        def __init__(self, e, r):
                            self.e = e
                            self.r = r

                        def get(self):
                            key = self.e.get()
                            return key[self.r.keyfields[0]]

                    entries[c] = hide_get(entry, reference)

                elif c in self.table.keyfields and self.table.autoincr:
                    ttk.Label(win, text=c).grid(in_=win_frame, row=i, sticky="e")
                    entry = ttk.Entry(win)
                    entry.insert(0, "will be entered automatically")
                    entry.configure(state="readonly")
                    entry.grid(in_=win_frame, row=i, column=1, sticky="w")

                else:
                    ttk.Label(win, text=c).grid(in_=win_frame, row=i, sticky="e")
                    entry = ttk.Entry(win)
                    entry.grid(in_=win_frame, row=i, column=1, sticky="w")
                    entries[c] = entry

            ttk.Button(win,
                       text="Insert",
                       command=lambda: self.create(
                           {c: e.get() for c, e in entries.items()})
                       ).grid(in_=win_frame, column=1, sticky="e")

        if not selection:
            popup.add_command(label="Insert", command=insert)
        elif len(selection) > 1:
            popup.add_command(label="Delete all", command=delete)
        else:
            popup.add_command(label="Delete", command=delete)

        return popup

    def _place_popup_menu(self, x, y):
        self.popup.post(x, y)
        self.popup.grab_release()

    def _destroy_popup_menu(self):
        if self.popup:
            self.popup.destroy()
            self.popup = None

    def __on_click(self, event):
        self._destroy_popup_menu()

    def __on_right_click(self, event):
        self._destroy_popup_menu()
        self.popup = self._create_popup_menu()
        self._place_popup_menu(event.x_root, event.y_root)

    def __on_changed(self, row, col, oldvalue):
        colname = self._tree.heading(col, "text")
        key = self._get_key(row)
        if colname in self.table.keyfields:
            key[colname] = oldvalue

        value = self.set(row, col)
        try:
            self.table.set(key, **{colname: value})
        except ModelError as e:
            # XXX: we must use the internal call here otherwise we'll call
            # ourself again and BOOM, maximum recursion
            self._tree.set(row, col, oldvalue)
            ErrorView(e)
