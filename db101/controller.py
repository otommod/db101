from .views import ErrorView, TableView
from .models import InvalidOperationError


class TableController:
    def __init__(self, tablemodel, parent):
        self.m = tablemodel
        self.v = TableView(parent, self.m)

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
