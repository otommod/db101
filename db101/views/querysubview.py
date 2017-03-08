from tkinter import ttk


class QuerySubView(ttk.Frame):
    @classmethod
    def lookup(cls, query, *args, **kwargs):
        return {
            "How many drugs do we sell?": HowManyDrugsWeSell,
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
