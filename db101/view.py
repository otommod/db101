import tkinter as tk
from tkinter import ttk

from .observable import eventsource
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
        self.popup = None

        self.tree.tree.bind("<1>", self.on_click, add="+")
        self.tree.tree.bind("<3>", self.on_right_click, add="+")
        self.tree.cell_edited.add_observer(self.on_changed)

        self.tree.add_items(self.get_data())

    def get_data(self):
        values = self.t.get()
        return [tuple("―" if i is None else i for i in v) for v in values]

    def _create_popup_menu(self):
        popup = tk.Menu(self.tree, tearoff=False)

        def delete():
            selection = self.tree.tree.selection()
            for item in selection:
                key = {k: self.tree.set(item, k) for k in self.t.key}
                self.t.delete(key)

        popup.add_command(label="delete", command=delete)
        # for i in ("one", "two", "three"):
        #     menu.add_command(label=i)

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

    def on_changed(self, row, col, old_value):
        colname = self.tree.tree.heading(col, "text")
        key = {k: self.tree.set(row, k) for k in self.t.key}
        if colname in key:
            key[colname] = old_value
        print(key)

        update = {colname: self.tree.set(row, col)}
        self.t.set(key, **update)
