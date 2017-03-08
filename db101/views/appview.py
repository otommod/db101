import tkinter as tk
from tkinter import ttk
from functools import partial

from ..observable import eventsource

QUERIES = [
    "How many drugs do we sell?",
    "What drugs could we sell?",
]


class AppView(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.subview = None
        self.results = ttk.Frame(self)
        self.results.grid(row=0, column=0)

        first_choice = None
        choice_var = tk.StringVar()
        choices = ttk.LabelFrame(self, text="Queries")
        choices.grid(row=0, column=1)
        for q in QUERIES:
            radio = ttk.Radiobutton(self, text=q,
                                    variable=choice_var, value=q,
                                    command=partial(self.query_selected, q))
            radio.grid(in_=choices, sticky="w")
            if first_choice is None:
                first_choice = radio

        button_group = ttk.Frame(self)
        button_group.grid(row=0, column=2, sticky="n")
        ttk.Button(self, text="Search", command=self.search_request) \
            .grid(in_=button_group, row=0, column=0, sticky="n")
        ttk.Button(self, text="Tables", command=self.tables_please) \
            .grid(in_=button_group, row=1, column=0, sticky="n")

        first_choice.invoke()

    @eventsource
    def query_selected(query):
        pass

    @eventsource
    def search_request():
        pass

    @eventsource
    def tables_please():
        pass

    def add_subview(self, query_view):
        self.clear_subview()

        self.subview = query_view
        self.subview.grid(in_=self, row=0, column=0)

    def clear_subview(self):
        if self.subview is not None:
            self.subview.grid_forget()
            self.subview.destroy()
            self.subview = None
