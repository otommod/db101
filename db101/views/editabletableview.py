import tkinter as tk
# from tkinter import ttk

from ..observable import eventsource
from ..widgets import EditableMultiColumnList
from .tableview import TableView


class EditableTableView(TableView, EditableMultiColumnList):
    def __init__(self, parent, table):
        self.popup = None
        super().__init__(parent, table)

        self._tree.bind("<1>", self.on_click, add="+")
        self._tree.bind("<3>", self.on_right_click, add="+")
        self.cell_edited.add_observer(self.on_changed)

        # debug
        self.update.add_observer(lambda *a: print("EditableTableView", a))

    @eventsource
    def update(key, changes):
        pass

    @eventsource
    def delete(keys):
        pass

    def fill(self):
        self._destroy_popup_menu()
        super().fill()

    def _get_key(self, item):
        return {k: self.tree.set(item, k) for k in self.m.key}

    def _create_popup_menu(self):
        popup = tk.Menu(self.tree, tearoff=False)
        selection = self.tree._tree.selection()

        def delete():
            self.delete(self._get_key(item) for item in selection)

        def insert():
            pass

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

    def on_click(self, event):
        self._destroy_popup_menu()

    def on_right_click(self, event):
        self._destroy_popup_menu()
        self.popup = self._create_popup_menu()
        self._place_popup_menu(event.x_root, event.y_root)

    def on_changed(self, row, col, new_value):
        colname = self.tree._tree.heading(col, "text")
        self.update(self._get_key(row),
                    {colname: new_value})
