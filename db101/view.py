import tkinter as tk
from tkinter import ttk

from .observable import event
from .widgets import EditableTreeview


class View(tk.Toplevel):
    def __init__(self, parent):
        super(View, self).__init__(parent)
        self.protocol("WM_DELETE_WINDOW", self.master.destroy)

        ttk.Label(self, text="my money").grid(column=1, row=1, sticky=(tk.W, tk.E))
        self.moneyCtrl = ttk.Entry(self, width=8)
        self.moneyCtrl.grid(column=1, row=2, sticky=(tk.W, tk.E))

        self.add_btn = ttk.Button(self, text="Add", width=8)
        self.add_btn.grid(column=1, row=3, sticky=tk.W)

        self.withdraw_btn = ttk.Button(self, text="Withdraw", width=8)
        self.withdraw_btn.grid(column=2, row=3, sticky=tk.E)

    def set_money(self, money):
        self.moneyCtrl.delete(0, "end")
        self.moneyCtrl.insert("end", str(money))



class TableView:
    def __init__(self, parent, table):
        self.t = table
        self.tree = EditableTreeview(parent, self.t.fields)

        self.tree.add_items(self.t.get())

        self.tree.cell_edited.add_observer(self.on_changed)

    def on_changed(self, row, col, old_value):
        colname = self.tree.tree.heading(col, "text")
        key = {k: self.tree.set(row, k) for k in self.t.key}
        if colname in key:
            key[colname] = old_value
        print(key)
