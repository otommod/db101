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

        self.tree = ttk.Treeview(self, show="headings", columns=columns)
        vsb = EventedScrollbar(self, orient="vertical", command=self.yview)
        hsb = EventedScrollbar(self, orient="horizontal", command=self.xview)
        self.tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        vsb.scrolled.add_observer(lambda *ignore: self.view_changed())
        hsb.scrolled.add_observer(lambda *ignore: self.view_changed())

        for c in columns:
            self.tree.heading(c, text=c)
            self.tree.column(c, stretch=True)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.tree.grid(row=0, column=0, sticky="nsew",  padx=2, pady=2)
        vsb.grid(row=0, column=1, sticky="ns",     padx=2, pady=2)
        hsb.grid(row=1, column=0, sticky="ew",     padx=2, pady=2)

        self.cell_entry = None
        self.tree.bind("<1>", lambda *ignore: self.cancel_edit())
        self.tree.bind("<Double-1>", self.on_double_click)
        self.tree.bind("<3>", self.on_right_click)

    @eventsource
    def view_changed():
        pass

    @eventsource
    def cell_edited(row, col, old_value):
        pass

    def xview(self, *args):
        curview = self.tree.xview()
        self.tree.xview(*args)
        if curview != self.tree.xview():
            self.view_changed()

    def yview(self, *args):
        curview = self.tree.yview()
        self.tree.yview(*args)
        if curview != self.tree.yview():
            self.view_changed()

    def set(self, item, column=None, value=None):
        old_value = self.tree.set(item, column)
        result = self.tree.set(item, column, value)
        if column is not None and value is not None:
            self.cell_edited(item, column, old_value)
        return result

    def _resize_columns(self):
        """Adjust columns' width if necessary to fit every value."""

        for c in self.columns:
            needed_width = max(font_width(self.set(i, c)) for i in
                               self.tree.get_children(""))
            if self.tree.column(c, option="width") < needed_width:
                self.tree.column(c, width=needed_width)

    def add_item(self, item):
        self.tree.insert("", "end", values=item)
        self._resize_columns()

    def add_items(self, items):
        for i in items:
            self.tree.insert("", "end", values=i)
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

        entry = ttk.Entry(self.tree)
        entry.insert(0, value)

        # entry['state'] = 'readonly'
        # entry['exportselection'] = False
        # entry['selectbackground'] = '#1BA1E2'
        # entry['readonlybackground'] = 'white'

        def commit_entry(*ignore):
            self.set(row, col, entry.get())
            entry.destroy()

        entry.focus_force()
        entry.bind("<Return>", commit_entry)
        entry.bind("<Escape>", lambda *ignore: entry.destroy())
        return entry

    def _place_cell_entry(self, row, col):
        bbox = self.tree.bbox(row, col)
        if not bbox:
            self.cell_entry.place_forget()
            return
        x, y, width, height = bbox
        self.cell_entry.place(x=x, y=y, width=width, height=height)

    def on_double_click(self, event):
        self.edit_cell(self.tree.identify_row(event.y),
                       self.tree.identify_column(event.x))

    def on_right_click(self, event):
        selection = self.tree.selection()
        clicked_on = self.tree.identify_row(event.y)
        print(selection)
        if clicked_on not in selection:
            self.tree.selection_set(clicked_on)
