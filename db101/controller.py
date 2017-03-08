import tkinter as tk

from . import models
from .exceptions import ModelError
from .views import (EditableTableView, ErrorView, MainView, QuerySubView,
                    TableView)


class MainController:
    def __init__(self, model):
        self.model = model

        self.root = tk.Tk()
        self.root.title("BaseMasteRX 3000")
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)

        self.view = MainView(self.root, model)
        self.root.geometry("683x384")
        self.view.grid(sticky="nsew")

        self.view.table_request.add_observer(self.__on_table_request)

        self.root.mainloop()

    def __on_table_request(self, table):
        table_model = models.NamedTable.lookup(table)
        table_view = EditableTableView(self.view, table_model)
        self.view.add_table(table, table_view)
