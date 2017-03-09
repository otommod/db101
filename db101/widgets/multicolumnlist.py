import tkinter as tk
from tkinter import font, ttk

from ..observable import eventsource
from .eventedscrollbar import EventedScrollbar


def font_width(text):
    return font.Font().measure(text)


class MultiColumnList(ttk.Frame):
    def __init__(self, parent, columns):
        super(MultiColumnList, self).__init__(parent)
        self.columns = columns

        s = ttk.Style()
        s.configure("Multicolumn.TFrame", background="red")
        self.configure(style="Multicolumn.TFrame")

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

        self._tree.grid(row=0, column=0, sticky="nsew")
        vsb.grid(row=0, column=1, sticky="ns")
        hsb.grid(row=1, column=0, sticky="ew")

        for c in self.winfo_children():
            c.grid_configure(padx=2, pady=2)

        self._tree.bind("<3>", self.__on_right_click)

    @eventsource
    def view_changed():
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
        return self._tree.set(item, column, value)

    def _resize_columns(self):
        """Adjust columns' width if necessary to fit every value."""

        for c in self.columns:
            try:
                needed_width = max(font_width(self.set(i, c))
                                   for i in self._tree.get_children(""))
            except ValueError:
                needed_width = 0
            if self._tree.column(c, option="width") < needed_width:
                self._tree.column(c, width=needed_width)

    def clear(self):
        for i in self._tree.get_children(""):
            self._tree.delete(i)

    def add_item(self, item):
        self._tree.insert("", "end", values=item)
        self._resize_columns()

    def add_items(self, items):
        for i in items:
            self._tree.insert("", "end", values=i)
        self._resize_columns()

    def __on_right_click(self, event):
        selection = self._tree.selection()
        clicked_on = self._tree.identify_row(event.y)
        print("selected", selection)
        if clicked_on not in selection:
            self._tree.selection_set(clicked_on)
