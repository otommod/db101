import tkinter as tk
from tkinter import ttk

from .querysubview import QuerySubView


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

        menudesc = {
            "Find": {
                "__command__": self.show_query,
                "How many drugs do we sell?": "",
                "Oldest People Drugs": "",
                "Drugs Capacity": "",
                "Last telephone calls": "",
                "Our Drug Companies": "",
                "Other Drug Companies": "",
                "New Drugs From Partners": "",
                "New Drugs From Other Companies": "",
                "Drugs For A Patient": "",
                "Number Of Contracts Order By Start Date": "",
                "Number Of Contracts Order By End Date": "",
                "Doctors With Average Patients Over 50": "",
            },

            "Search for": {
                "Doctor": "",
                "Patient": "",
                "Drug": "",
                "Pharmacies": "",
                "Prescription": "",
            },

            "View table": {
                "Patients": "",
                "Doctors": "",
                "Drugs": "",
                "Pharmacies": "",
                "Prescriptions": "",
            }
        }

        menubar = create_menu(parent, menudesc)
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

        if self.query_tab is not None:
            self.tabs.hide(self.query_tab)
            self.tabs.forget(self.query_tab)
            self.query_tab = None

        self.tabs.add(query_view, text="Query")
        self.query_tab = self.tabs.index("current")
