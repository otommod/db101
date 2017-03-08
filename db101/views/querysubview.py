from tkinter import ttk
from . import TableView


class QuerySubView(ttk.Frame):
    @classmethod
    def lookup(cls, query, *args, **kwargs):
        return {
            "How many drugs do we sell?": HowManyDrugsWeSell,
            "What drugs could we sell?": PotentialDrugs,
        }[query]


class HowManyDrugsWeSell(QuerySubView):
    def __init__(self, parent, model):
        super().__init__(parent)
        self.label = ttk.Label(self)

        ttk.Label(self, text="Our pharmacy is currently selling").grid()
        self.label.grid()
        ttk.Label(self, text="different drug(s)").grid()

        self.count = model.count_drugs_on_sale()
        self.count.changed.add_observer(self.render)
        self.render()

    def render(self):
        number = self.count.get()
        self.label.configure(text=str(number))


class PotentialDrugs(QuerySubView):
    def __init__(self, parent, pharmacy):
        super().__init__(parent)
        self.pharmacy = pharmacy
        self.drugs = pharmacy.potential_drugs()
        self.table = TableView(self, self.drugs)

        ttk.Label(self, text=("These are the drugs from our partnered"
                              " companies that we do not sell")).grid()
        self.table.grid()

        self.render()

    def render(self):
        pass
