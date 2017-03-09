from .tableview import TableView
from ..observable import eventsource


class SingleSelectionTableView(TableView):
    def __init__(self, parent, table):
        super().__init__(parent, table)
        self._tree.bind("<Double-1>", self.__on_double_click, add="+")

    @eventsource
    def selected(key):
        pass

    def __on_double_click(self, event):
        self.selected(self._get_key(
            self._tree.identify_row(event.y)))
