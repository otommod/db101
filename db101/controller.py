from .views import ErrorView, TableView, QuerySubView
from .exceptions import InvalidOperationError


class TableController:
    def __init__(self, model, view):
        self.m = model
        self.v = view
        self.v.fill()

        self.v.update.add_observer(self.on_update)
        self.v.delete.add_observer(self.on_delete)

    def on_update(self, key, changes):
        try:
            self.m.set(key, **changes)
        except InvalidOperationError as e:
            ErrorView(e)

    def on_delete(self, keys):
        try:
            for k in keys:
                self.m.delete(k)
        except InvalidOperationError as e:
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

        model = getattr(self.m, search_type)
        model.bake(**params)

        self.search_results = TableView(self.search_form, model)
        self.search_results.grid(row=2, column=0, columnspan=5)


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
        self.view.show_query(query_view)

    def on_search(self):
        pass

    def on_tables(self):
        pass
