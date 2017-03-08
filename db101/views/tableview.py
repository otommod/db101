from ..widgets import MultiColumnList


class TableView(MultiColumnList):
    def __init__(self, parent, table):
        super().__init__(parent, table.fields)
        self.table = table

        self.table.changed.add_observer(self.fill)
        self.fill()

    def fill(self):
        # replace any NULLs with a long dash
        self.clear()
        self.add_items([("\u2015" if c is None else c) for c in r]
                       for r in self.table.get())
