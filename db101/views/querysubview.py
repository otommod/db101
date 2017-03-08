from tkinter import ttk


class QuerySubView(ttk.Frame):
    @classmethod
    def from_query(cls, query, *args, **kwargs):
        return {
            "How many drugs do we sell?": HowManyDrugsWeSell,
        }[query](*args, **kwargs)

    def __init__(self, parent, model):
        super().__init__(parent)
        self.model = model


class HowManyDrugsWeSell(QuerySubView):
    def __init__(self, parent, model):
        super().__init__(parent, model)

        ttk.Label(self, text="Our pharmacy is currently selling").grid()

        self.label = ttk.Label(self)
        self.label.grid()

        ttk.Label(self, text="different drug(s)").grid()

        self.model.changed.add_observer(self.render)
        self.render()

    def render(self):
        number = self.model.count_drugs_on_sale()
        self.label.configure(text=str(number))
