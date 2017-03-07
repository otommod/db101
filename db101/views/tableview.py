from ..observable import eventsource
from ..widgets import MultiColumnList


class TableView(MultiColumnList):
    def __init__(self, parent, table):
        super().__init__(parent, table.fields)
        self.m = table

        self.fill()
        self.m.changed.add_observer(self.fill)

        # debug
        self.m.changed.add_observer(print)

    def fill(self):
        # replace any NULL values with an em dash
        self.clear()
        self.add_items(["―" if i is None else i for i in v]
                            for v in self.m.get())
