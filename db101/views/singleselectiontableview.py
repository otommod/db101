from .tableview import TableView


class SingleSelectionTableView(TableView):
    def __init__(self, parent, table):
        super().__init__(parent, table)
        self._tree.configure(selectmode="browse")

    def get(self):
        selection = self._tree.selection()
        return self._get_key(selection)
