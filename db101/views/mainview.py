import tkinter as tk
from tkinter import ttk
from functools import partial

from . import MultiSearchView, QuerySubView
from ..observable import eventsource


def nop(*a, **kw):
    pass


def create_menu(parent, menudef):
    command = menudef.get("__command__", nop)

    menu = tk.Menu(parent)
    for n, c in menudef.items():
        if isinstance(c, dict):
            m = create_menu(parent, c)
            menu.add_cascade(label=n, menu=m)
        else:
            menu.add_command(label=n, command=lambda n=n: command(n))
    return menu


class MainView(ttk.Frame):
    def __init__(self, parent, model):
        super().__init__(parent)
        self.model = model
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        s = ttk.Style()
        s.configure("Main.TFrame", background="black")
        # bg_image = tk.PhotoImage(file="./basemasterx3000.png")

        self.bg_label = ttk.Label(self, style="Main.TFrame")
        self.bg_label.grid(sticky="nsew")

        menubar = tk.Menu(self.master)

        query_menu = tk.Menu(menubar)
        for q in ["How many drugs do we sell?",
                  "Oldest People Drugs",
                  "Drugs Capacity",
                  "Last telephone calls",
                  "Our Drug Companies",
                  "Other Drug Companies",
                  "New Drugs From Partners",
                  "New Drugs From Other Companies",
                  "Drugs For A Patient",
                  "Number Of Contracts Order By Start Date",
                  "Number Of Contracts Order By End Date",
                  "Doctors With Average Patients Over 50"]:
            query_menu.add_command(label=q,
                                   command=partial(self.show_query, q))
        menubar.add_cascade(label="Find", menu=query_menu)

        search_menu = tk.Menu(menubar)
        for s in ["Patient",
                  "Doctor",
                  "Drug",
                  # "Pharmaceuticals",
                  "Prescription"]:
            search_menu.add_command(label=s,
                                    command=partial(self.__on_search_click, s))
        menubar.add_cascade(label="Search for", menu=search_menu)

        tables_menu = tk.Menu(menubar)
        for t in ["Patient",
                  "Doctor",
                  "Drug",
                  "Pharmacy",
                  "Pharmaceutical",
                  "Prescription"]:
            tables_menu.add_command(label=t,
                                    command=partial(self.__on_table_click, t))
        menubar.add_cascade(labe="View table", menu=tables_menu)

        parent.config(menu=menubar)

        self.tabs = None
        self.query_tab = None
        self.query_frame = ttk.Frame(self)
        self.table_tabs = {}
        self.search_tabs = {}

    def _ensure_tabs(self):
        if self.tabs is None:
            self.bg_label.grid_forget()
            self.bg_label.destroy()

            self.tabs = ttk.Notebook(self)
            self.tabs.grid(row=0, column=0, sticky="nsew")

    def show_query(self, queryname):
        self._ensure_tabs()

        QueryView = QuerySubView.lookup(queryname)
        query_view = QueryView(self, self.model)

        if self.query_tab is None:
            self.tabs.add(query_view, text="Query")
            self.query_tab = self.tabs.index("end")
        else:
            self.tabs.hide(self.query_tab)
            self.tabs.forget(self.query_tab)
            self.tabs.insert(self.query_tab, query_view, text="Query")

    def __on_search_click(self, search_name):
        self._ensure_tabs()

        search_type = search_name.lower()
        if search_type == "pharmaceutical":
            search_type = "bigpharma"

        if search_type not in self.search_tabs:
            search_view = MultiSearchView.lookup(search_type)
            self.tabs.add(search_view(self.tabs, self.model),
                          text="%s search" % search_name)
            self.search_tabs[search_type] = self.tabs.index("end") - 1

        self.tabs.select(self.search_tabs[search_type])

    def __on_table_click(self, tablename):
        table = tablename.lower()
        if table == "pharmaceutical":
            table = "bigpharma"

        if table in self.table_tabs:
            self.tabs.select(self.table_tabs[table])
        else:
            self.table_request(table)

    def add_table(self, table, tableview):
        self._ensure_tabs()

        self.tabs.add(tableview, text="Table %s" % table)
        self.table_tabs[table] = self.tabs.index("end") - 1
        self.tabs.select(self.table_tabs[table])

    @eventsource
    def table_request(tablename):
        pass
