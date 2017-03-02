import tkinter as tk
from tkinter import ttk

from .observable import event


class Model:
    def __init__(self):
        self.money = 0

    @event
    def money_changed(new_amount):
        pass

    @property
    def money(self):
        return self._money

    @money.setter
    def money(self, new_amount):
        self._money = new_amount
        self.money_changed(new_amount)

    def add_money(self, value):
        self.money += value

    def withdraw(self, value):
        self.money -= value


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


class Controller:
    def __init__(self, root):
        self.model = Model()
        self.model.money_changed.add_observer(self.on_money_change)

        self.frame = ttk.Frame(root, padding="3 3 12 12")
        self.frame.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(0, weight=1)

        self.view = View(self.frame)
        self.view.add_btn.config(command=self.add_money)
        self.view.withdraw_btn.config(command=self.withdraw)

        # for child in self.frame.winfo_children():
        #     child.grid_configure(padx=5, pady=5)

        self.on_money_change(self.model.money)

    def add_money(self):
        self.model.add_money(10)

    def withdraw(self):
        self.model.withdraw(10)

    def on_money_change(self, new_amount):
        self.view.set_money(new_amount)
