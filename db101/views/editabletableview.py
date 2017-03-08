import tkinter as tk
from tkinter import ttk

from ..observable import eventsource
from ..widgets import EditableMultiColumnList
from .tableview import TableView


class EditableTableView(TableView, EditableMultiColumnList):
    def __init__(self, parent, table):
        self.popup = None
        super().__init__(parent, table)

        self._tree.bind("<1>", self.__on_click, add="+")
        self._tree.bind("<3>", self.__on_right_click, add="+")
        self.cell_edited.add_observer(self.__on_changed)

        self.created.add_observer(print)

    @eventsource
    def update(key, changes):
        pass

    @eventsource
    def delete(keys):
        pass

    @eventsource
    def created(new_item):
        pass

    def fill(self):
        self._destroy_popup_menu()
        super().fill()

    def _get_key(self, item):
        return {k: self._tree.set(item, k) for k in self.m.key}

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
            for i, c in enumerate(self.columns):
                ttk.Label(win, text=c).grid(in_=win_frame, row=i, sticky="e")
                entry = ttk.Entry(win)
                entry.grid(in_=win_frame, row=i, column=1, sticky="w")
                entries[c] = entry

            ttk.Button(win,
                       text="Insert",
                       command=lambda: self.created(
                           {c: e.get() for c, e in entries.items()})
                       ).grid(in_=win_frame, sticky="e")

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

    def __on_changed(self, row, col, new_value):
        colname = self._tree.heading(col, "text")
        self.update(self._get_key(row),
                    {colname: new_value})
