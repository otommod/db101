import tkinter as tk
from tkinter import font, ttk

from ..observable import eventsource
# from .singleentry import SingleEntry
from .eventedscrollbar import EventedScrollbar


def font_width(text):
    return font.Font().measure(text)


class EditableTreeview(ttk.Frame):
    def __init__(self, parent, columns):
        super(EditableTreeview, self).__init__(parent)
        self.columns = columns

        s = ttk.Style()
        s.configure("Editable.TFrame", background="red")
        self.configure(style="Editable.TFrame")

        self._tree = ttk.Treeview(self, show="headings", columns=columns)
        vsb = EventedScrollbar(self, orient="vertical", command=self.yview)
        hsb = EventedScrollbar(self, orient="horizontal", command=self.xview)
        self._tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        vsb.scrolled.add_observer(lambda *ignore: self.view_changed())
        hsb.scrolled.add_observer(lambda *ignore: self.view_changed())

        for c in columns:
            self._tree.heading(c, text=c)
            self._tree.column(c, stretch=True)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self._tree.grid(row=0, column=0, sticky="nsew",  padx=2, pady=2)
        vsb.grid(row=0, column=1, sticky="ns",     padx=2, pady=2)
        hsb.grid(row=1, column=0, sticky="ew",     padx=2, pady=2)

        self.cell_entry = None
        self._tree.bind("<1>", lambda *ignore: self.cancel_edit())
        self._tree.bind("<Double-1>", self.on_double_click)
        self._tree.bind("<3>", self.on_right_click)

    @eventsource
    def view_changed():
        pass

    @eventsource
    def cell_edited(row, col, new_value):
        pass

    def xview(self, *args):
        curview = self._tree.xview()
        self._tree.xview(*args)
        if curview != self._tree.xview():
            self.view_changed()

    def yview(self, *args):
        curview = self._tree.yview()
        self._tree.yview(*args)
        if curview != self._tree.yview():
            self.view_changed()

    def set(self, item, column=None, value=None):
        if column is not None and value is not None:
            self.cell_edited(item, column, value)
        try:
            return self._tree.set(item, column, value)
        except tk.TclError:
            # We shall assume that this means that an observer changed the tree
            # and now our items and columns are no longer valid.  This is fine.
            pass

    def _resize_columns(self):
        """Adjust columns' width if necessary to fit every value."""

        for c in self.columns:
            needed_width = max(font_width(self.set(i, c)) for i in
                               self._tree.get_children(""))
            if self._tree.column(c, option="width") < needed_width:
                self._tree.column(c, width=needed_width)

    def clear(self):
        self.cancel_edit()
        for i in self._tree.get_children(""):
            self._tree.delete(i)

    def add_item(self, item):
        self._tree.insert("", "end", values=item)
        self._resize_columns()

    def add_items(self, items):
        for i in items:
            self._tree.insert("", "end", values=i)
        self._resize_columns()

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

    def on_double_click(self, event):
        self.edit_cell(self._tree.identify_row(event.y),
                       self._tree.identify_column(event.x))

    def on_right_click(self, event):
        selection = self._tree.selection()
        clicked_on = self._tree.identify_row(event.y)
        print(selection)
        if clicked_on not in selection:
            self._tree.selection_set(clicked_on)
