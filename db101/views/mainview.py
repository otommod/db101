import tkinter as tk
from tkinter import ttk
from functools import partial

from .. import models
from .editabletableview import EditableTableView
from .tableview import TableView
from .querysubview import QuerySubView
from .searchview import SearchView
from .singleselectiontableview import SingleSelectionTableView


class MainView(ttk.Frame):
    def __init__(self, parent, general_model, pharmacy_cls):
        super().__init__(parent)
        self.general_model = general_model
        self.pharmacy_cls = pharmacy_cls
        self.pharmacy = None
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        s = ttk.Style()
        s.configure("Main.TFrame", background="black")
        bg_image = tk.PhotoImage(file="./basemasterx3000.png")

        self.bg_label = ttk.Label(self, style="Main.TFrame")
        self.bg_label.grid(sticky="nsew")

        menubar = tk.Menu(self.master)

        general_menu = tk.Menu(menubar, tearoff=False)
        for g in ["Total patient count",
                  "The Doctors and their patients",
                  "Number of pharmacies selling each drug",
                  "The drugs of patient...",
                  "The drugs that older people use",
                  "The doctors of old patients",
                  ]:
            general_menu.add_command(label=g,
                                     command=partial(self.__on_query_click, g,
                                                     self.general_model))
        menubar.add_cascade(label="General info", menu=general_menu)

        self.query_menu = tk.Menu(menubar, tearoff=False)
        self.query_menu.add_command(label="Login", command=self.login_form)
        menubar.add_cascade(label="Our Pharmacy", menu=self.query_menu)

        self.search_menu = tk.Menu(menubar, tearoff=False)
        self.search_menu.add_command(label="Login", command=self.login_form)
        menubar.add_cascade(label="Search for", menu=self.search_menu)

        tables_menu = tk.Menu(menubar, tearoff=False)
        for t in ["Patient",
                  "Doctor",
                  "Drug",
                  "Pharmacy",
                  "Pharmaceutical",
                  "Prescription",
                  "Contract",
                  "ActiveContracts",
                  "Phones"]:
            tables_menu.add_command(label=t,
                                    command=partial(self.__on_table_click, t))
        menubar.add_cascade(labe="View table", menu=tables_menu)

        parent.config(menu=menubar)

        self.tabs = None
        self.query_tab = None
        self.query_frame = ttk.Frame(self)
        self.table_tabs = {}
        self.search_tabs = {}

    def login_form(self):
        win = tk.Toplevel(self.master)
        win.title("Pharmacy login")

        entry = SingleSelectionTableView(win,
                                         models.NamedTable.lookup("pharmacy"))
        entry.grid()

        def login(e):
            pharmid = entry.get()
            win.destroy()
            self.login(pharmid["id"])

        win.bind("<Escape>", lambda e: win.destroy())
        entry._tree.bind("<Double-1>", login, add="+")

    def login(self, pharmacy_id):
        self.pharmacy = self.pharmacy_cls({
            "our_pharmacy": pharmacy_id  # this is so leaky it's not even an
        })                               # abstraction anymore

        # excuse my code... it's late, I haven't slept in days and the deadline
        # is tommorow
        self.query_menu.delete(0)
        for q in ["Our customers",
                  "How many drugs do we sell?",
                  "What drugs do we sell?",
                  "What drugs could we sell?",
                  "Contracts closest due",
                  "Contracts that end before...",
                  "Partnered Pharmaceuticals",
                  "Not partnered Pharmaceuticals",
                  "Potential future partners"]:
            self.query_menu.add_command(label=q, command=partial(
                self.__on_query_click, q, self.pharmacy))

        self.search_menu.delete(0)
        for s in ["Patient",
                  "Doctor",
                  "Drug",
                  # "Pharmaceuticals",
                  "Prescription"]:
            self.search_menu.add_command(label=s, command=partial(
                self.__on_search_click, s))

    def _ensure_tabs(self):
        if self.tabs is None:
            self.bg_label.grid_forget()
            self.bg_label.destroy()

            self.tabs = ttk.Notebook(self)
            self.tabs.grid(row=0, column=0, sticky="nsew")

    def __on_query_click(self, queryname, model):
        self._ensure_tabs()

        QueryView = QuerySubView.lookup(queryname)
        query_view = QueryView(self, model)

        if self.query_tab is not None:
            self.tabs.hide(self.query_tab)
            self.tabs.forget(self.query_tab)

        self.tabs.add(query_view, text="Query")
        self.query_tab = self.tabs.index("end") - 1
        self.tabs.select(self.query_tab)

    def __on_search_click(self, search_name):
        self._ensure_tabs()

        search_type = search_name.lower()
        if search_type == "pharmaceutical":
            search_type = "bigpharma"

        if search_type not in self.search_tabs:
            search_view = SearchView.lookup(search_type)
            self.tabs.add(search_view(self.tabs, self.pharmacy),
                          text="%s search" % search_name)
            self.search_tabs[search_type] = self.tabs.index("end") - 1

        self.tabs.select(self.search_tabs[search_type])

    def __on_table_click(self, tablename):
        self._ensure_tabs()

        table = tablename.lower()
        if table == "pharmaceutical":
            table = "bigpharma"

        if table not in self.table_tabs:
            table_model = models.NamedTable.lookup(table)
            if table == "phones":
                # Non editable
                table_view = TableView(self, table_model)
            else:
                table_view = EditableTableView(self, table_model)
            self.tabs.add(table_view, text="Table %s" % tablename)
            self.table_tabs[table] = self.tabs.index("end") - 1

        self.tabs.select(self.table_tabs[table])
