import tkinter as tk

from . import models
from .exceptions import ModelError
from .views import (EditableTableView, ErrorView, MainView, QuerySubView,
                    TableView)


class TableController:
    def __init__(self, model, view):
        self.m = model
        self.v = view
        self.v.fill()

        self.v.update.add_observer(self.on_update)
        self.v.delete.add_observer(self.on_delete)
        self.v.created.add_observer(self.on_insert)

    def on_update(self, key, changes):
        try:
            self.m.set(key, **changes)
        except ModelError as e:
            ErrorView(e)

    def on_delete(self, keys):
        try:
            for k in keys:
                self.m.delete(k)
        except ModelError as e:
            ErrorView(e)

    def on_insert(self, new_item):
        try:
            self.m.append(new_item)
        except ModelError as e:
            ErrorView(e)


class SearchController:
    def __init__(self, pharmacy, view):
        self.pharmacy = pharmacy
        self.search_form = view
        self.search_results = None

        self.search_form.form_selected.add_observer(self.on_type_change)
        self.search_form.do_search.add_observer(self.on_search)

    def _clear_results(self):
        if self.search_results is not None:
            self.search_results.grid_forget()
            self.search_results.destroy()
            self.search_results = None

    def on_type_change(self):
        self._clear_results()

    def on_search(self, search_type, params):
        self._clear_results()

        model = getattr(self.pharmacy, search_type + "_search")(params)
        print(model)

        self.results_view = TableView(self.search_form, model)
        self.results_view.grid(row=2, column=0, columnspan=5)


class AppController:
    def __init__(self, view, pharmacy):
        self.view = view
        self.pharmacy = pharmacy

        self.view.query_selected.add_observer(self.on_query_selection)
        self.view.search_request.add_observer(self.on_search)
        self.view.tables_please.add_observer(self.on_tables)

    def on_query_selection(self, query):
        QueryView = QuerySubView.lookup(query)

        query_view = QueryView(self.view, self.pharmacy)
        self.view.add_subview(query_view)

    def on_search(self):
        pass

    def on_tables(self):
        pass


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

        table_controller = TableController(table_model, table_view)

        self.view.add_table(table, table_view)
