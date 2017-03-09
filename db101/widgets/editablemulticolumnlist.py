import tkinter as tk
from tkinter import font, ttk

from ..observable import eventsource
from .eventedscrollbar import EventedScrollbar
from .multicolumnlist import MultiColumnList


class EditableMultiColumnList(MultiColumnList):
    def __init__(self, parent, columns):
        super().__init__(parent, columns)

        s = ttk.Style()
        s.configure("Editable.TFrame", background="red")
        self.configure(style="Editable.TFrame")

        self.cell_entry = None
        self._tree.bind("<1>", self.__on_click)
        self._tree.bind("<Double-1>", self.__on_double_click)

    @eventsource
    def cell_edited(row, col, new_value):
        pass

    def set(self, item, column=None, value=None):
        old_val = self._tree.set(item, column)
        result = self._tree.set(item, column, value)
        if column is not None and value is not None:
            self.cell_edited(item, column, old_val)
        return result

    def clear(self):
        self.cancel_edit()
        super().clear()

    def edit_cell(self, row, col):
        self.cancel_edit()

        self.cell_entry = self._create_cell_entry(row, col)
        self._place_cell_entry(row, col)
        self.view_changed.add_observer(
            lambda: self._place_cell_entry(row, col))

    def cancel_edit(self):
        if self.cell_entry is not None:
            self.cell_entry.destroy()
            self.cell_entry = None

    def _create_cell_entry(self, row, col):
        value = self.set(row, col)

        entry = ttk.Entry(self._tree)
        entry.insert(0, value)

        def commit_entry(*ignore):
            self.set(row, col, entry.get())
            entry.destroy()

        entry.focus_force()
        entry.bind("<Return>", commit_entry)
        entry.bind("<Escape>", lambda *ignore: entry.destroy())
        return entry

    def _place_cell_entry(self, row, col):
        bbox = self._tree.bbox(row, col)
        if not bbox:
            self.cell_entry.place_forget()
            return
        x, y, width, height = bbox
        self.cell_entry.place(x=x, y=y, width=width, height=height)

    def __on_click(self, event):
        self.cancel_edit()

    def __on_double_click(self, event):
        self.edit_cell(self._tree.identify_row(event.y),
                       self._tree.identify_column(event.x))
