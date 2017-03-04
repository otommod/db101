from tkinter import ttk
from tkinter import font

from ..observale import event


def measure_width(text):
    return font.Font().measure(text)


class EntryPopup(ttk.Entry):
    def __init__(self, parent, callback, value="", **kwargs):
        super(EntryPopup, self).__init__(parent, **kwargs)
        self.callback = callback
        self.insert(0, value)

        # self['state'] = 'readonly'
        # self['exportselection'] = False
        # self['selectbackground'] = '#1BA1E2'
        # self['readonlybackground'] = 'white'

        self.focus_force()
        self.bind("<Return>", self.end_insert)
        self.bind("<Control-a>", self.select_all)
        self.bind("<Escape>", lambda *ignore: self.destroy())

    def select_all(self, *ignore):
        """Set selection on the whole text"""
        self.selection_range(0, "end")
        return "break"  # to interrupt default key-bindings

    def end_insert(self, *ignore):
        self.callback(self.get())
        self.destroy()


class EditableTreeview(ttk.Frame):
    def __init__(self, parent, columns):
        super(EditableTreeview, self).__init__(parent)
        # self.parent = parent
        self.i = 0
        self.columns = columns

        # self.columnconfigure(0, weight=1)
        # self.rowconfigure(0, weight=1)

        self.tree = ttk.Treeview(self, show="headings", columns=columns)
        vsb = ttk.Scrollbar(self, orient="vertical", command=self.yview)
        hsb = ttk.Scrollbar(self, orient="horizontal", command=self.xview)
        self.tree.configure(yscrollcommand=self.scroll_set(vsb),
                            xscrollcommand=self.scroll_set(hsb))

        for c in columns:
            self.tree.heading(c, text=c)
            self.tree.column(c, stretch=True)

        self.tree.grid(row=0, column=0, sticky="nsew")
        vsb.grid(row=0, column=1, sticky="ns")
        hsb.grid(row=1, column=0, sticky="ew")

        self.cell_entry = None
        self.tree.bind("<Double-1>", self.on_double_click)
        self.tree.bind("<1>", lambda *_: self.destroy_popups())

    @event
    def scrolled():
        pass

    def _scroll_set(self, scrollbar):
        def inner(*args, **kwargs):
            self.scrolled()
            return scrollbar.set(*args, **kwargs)
        return inner

    def xview(self, *args):
        preview = self.tree.xview()
        self.tree.xview(*args)
        if preview != self.tree.xview():
            self.scrolled()

    def yview(self, *args):
        preview = self.tree.yview()
        self.tree.yview(*args)
        if preview != self.tree.yview():
            self.scrolled()

    def add_item(self, item):
        self.tree.insert("", "end", values=item)
        self.i += 1

        self.resize_column()

    def add_items(self, items):
        for i in items:
            self.tree.insert("", "end", value=i)
            self.i += 1

        self.resize_column()

    def resize_column(self):
        """adjust column's width if necessary to fit each value"""

        for c in self.columns:
            col_w = max(measure_width(self.tree.set(i, c)) for i in
                        self.tree.get_children(""))
            if self.tree.column(c, option="width") < col_w:
                self.tree.column(c, width=col_w)

    def edit_cell(self, row, col):
        self.destroy_popups()
        value = self.tree.set(row, col)

        self.cell_entry = EntryPopup(
            self.tree, lambda val: self.tree.set(row, col, val), value)
        self.place_cell_entry(row, col)
        self.scrolled.add_observer(lambda: self.place_cell_entry(row, col))

    def destroy_popups(self):
        if self.cell_entry is not None:
            self.cell_entry.destroy()
            self.cell_entry = None

    def place_cell_entry(self, rowid, column):
        bbox = self.tree.bbox(rowid, column)
        if not bbox:
            self.cell_entry.place_forget()
            return

        x, y, width, height = bbox
        self.cell_entry.place(x=x, y=y, width=width, height=height)

    def on_double_click(self, event):
        self.edit_cell(self.tree.identify_row(event.y),
                       self.tree.identify_column(event.x))
