import tkinter as tk
from tkinter import ttk
from functools import partial

from . import TableView
from ..widgets import Spinbox
from ..observable import eventsource


class SearchForm(ttk.Frame):
    def __init__(self, parent, query):
        super().__init__(parent)
        self.query = query
        self.tableview = None

    @eventsource
    def do_search(search):
        pass

    def _do_search(self):
        self.do_search(self.query(self.get()))

    def get(self):
        return {k: v for k in self.ARGS
                for v in [getattr(self, k).get()] if v}


class DrugSearchForm(SearchForm):
    ARGS = {"bigpharma", "formula", "sold", "price_min", "price_max"}

    def __init__(self, parent, pharmacy):
        super().__init__(parent, pharmacy.drug_search)

        ttk.Label(self, text="Pharmacuetical").grid()
        self.bigpharma = ttk.Entry(self)
        self.bigpharma.grid(row=0, column=1, columnspan=4)

        ttk.Label(self, text="Formula").grid()
        self.formula = ttk.Entry(self)
        self.formula.grid(row=1, column=1, columnspan=4)

        self.sold = tk.StringVar()
        ttk.Label(self, text="Sold?").grid()
        ttk.Radiobutton(self, variable=self.sold, value="yes",
                        text="Yes").grid(row=2, column=1)
        ttk.Radiobutton(self, variable=self.sold, value="no",
                        text="No").grid(row=2, column=2)
        ttk.Radiobutton(self, variable=self.sold, value="dont_care",
                        text="Don't care").grid(row=2, column=3, columnspan=2)
        self.sold.set("dont_care")

        ttk.Label(self, text="Price").grid()

        ttk.Label(self, text="min:").grid(row=3, column=1)
        self.price_min = Spinbox(self, from_=0, to=float("Inf"), width=4)
        self.price_min.grid(row=3, column=2)

        ttk.Label(self, text="max:").grid(row=3, column=3)
        self.price_max = Spinbox(self, from_=0, to=float("Inf"), width=4)
        self.price_max.grid(row=3, column=4)

        ttk.Button(self, text="Search", command=self._do_search) \
            .grid(row=4, column=5)

    def get(self):
        vals = super().get()
        if "sold" in vals:
            vals["we_sell"] = vals["sold"] == "yes"
            vals["we_dont_sell"] = vals["sold"] == "no"

        vals["include_price"] = False
        if "price_min" in vals or "price_max" in vals:
            vals["include_price"] = True

            if vals["price_min"].isdigit():
                vals["price_min"] = vals["price_min"]
            else:
                vals["price_min"] = float("inf")

            if vals["price_max"].isdigit():
                vals["price_max"] = vals["price_max"]
            else:
                vals["price_max"] = -float("inf")
        return vals


class DoctorSearchForm(SearchForm):
    ARGS = {"name", "specialty", "exp", "patient", "drug"}

    def __init__(self, parent, model):
        super().__init__(parent, model.doctor_search)

        ttk.Label(self, text="Doctor Name").grid()
        self.name = ttk.Entry(self)
        self.name.grid(row=0, column=1)

        ttk.Label(self, text="Specialty").grid()
        self.specialty = ttk.Entry(self)
        self.specialty.grid(row=1, column=1)

        ttk.Label(self, text="Experience").grid()
        self.exp = Spinbox(self, from_=0, to=float("Inf"), width=3)
        self.exp.grid(row=2, column=1)

        ttk.Label(self, text="Patient Name").grid()
        self.patient = ttk.Entry(self)
        self.patient.grid(row=3, column=1)

        ttk.Label(self, text="Drug").grid()
        self.drug = ttk.Entry(self)
        self.drug.grid(row=4, column=1)

        ttk.Button(self, text="Search", command=self._do_search) \
            .grid(row=5, column=3)


class PatientSearchForm(SearchForm):
    ARGS = {"name", "doctor", "age_min", "age_max", "address", "drug"}

    def __init__(self, parent, model):
        super().__init__(parent, model.patient_search)

        ttk.Label(self, text="Name").grid()
        self.name = ttk.Entry(self)
        self.name.grid(row=0, column=1, columnspan=4)

        ttk.Label(self, text="Age").grid()

        ttk.Label(self, text="min:").grid(row=1, column=1)
        self.age_min = Spinbox(self, from_=0, to=float("Inf"), width=3)
        self.age_min.grid(row=1, column=2)

        ttk.Label(self, text="max:").grid(row=1, column=3)
        self.age_max = Spinbox(self, from_=0, to=float("Inf"), width=3)
        self.age_max.grid(row=1, column=4)

        ttk.Label(self, text="Address").grid()
        self.address = ttk.Entry(self)
        self.address.grid(row=2, column=1, columnspan=4)

        ttk.Label(self, text="Doctor").grid()
        self.doctor = ttk.Entry(self)
        self.doctor.grid(row=3, column=1, columnspan=4)

        ttk.Label(self, text="Drug").grid()
        self.drug = ttk.Entry(self)
        self.drug.grid(row=4, column=1, columnspan=4)

        ttk.Button(self, text="Search", command=self._do_search) \
            .grid(row=5, column=5)


# class BigPharmaSearchForm(SearchForm):
#     ARGS = {"name", "phone", "drug", "contract_start", "contract_end"}

#     def __init__(self, parent, model):
#         super().__init__(parent, model.bigpharma_search)

#         ttk.Label(self, text="Name").grid(row=0, column=0)
#         self.name = ttk.Entry(self)
#         self.name.grid(row=0, column=1)

#         ttk.Label(self, text="Phone").grid(row=1, column=0)
#         self.phone = ttk.Entry(self)
#         self.phone.grid(row=1, column=1)

#         ttk.Label(self, text="Drug").grid(row=2, column=0)
#         self.drug = ttk.Entry(self)
#         self.drug.grid(row=2, column=1)

#         ttk.Label(self, text="Contract Start").grid(row=3, column=0)
#         self.contract_start = ttk.Entry(self)
#         self.contract_start.grid(row=3, column=1)

#         ttk.Label(self, text="Contract End").grid(row=4, column=0)
#         self.contract_end = ttk.Entry(self)
#         self.contract_end.grid(row=4, column=1)

#         ttk.Button(self, text="Search",
#                    command=lambda: self.do_search(self.get())) \
#             .grid(row=5, column=3)


class PrescriptionSearchForm(SearchForm):
    ARGS = {"doctor", "patient", "date", "drug"}

    def __init__(self, parent, model):
        super().__init__(parent, model.prescription_search)

        ttk.Label(self, text="Doctor").grid(sticky="e")
        self.doctor = ttk.Entry(self)
        self.doctor.grid(row=0, column=1)

        ttk.Label(self, text="Patient").grid(sticky="e")
        self.patient = ttk.Entry(self)
        self.patient.grid(row=1, column=1)

        ttk.Label(self, text="Date").grid(sticky="e")
        self.date = ttk.Entry(self)
        self.date.grid(row=2, column=1)

        ttk.Label(self, text="Drug").grid(sticky="e")
        self.drug = ttk.Entry(self)
        self.drug.grid(row=3, column=1)

        ttk.Button(self, text="Search", command=self._do_search) \
            .grid(row=4, column=3)


ALL_FORMS = {
    "drug": DrugSearchForm,
    "doctor": DoctorSearchForm,
    "patient": PatientSearchForm,
    # "bigpharma": BigPharmaSearchForm,
    "prescription": PrescriptionSearchForm,
}


class SearchView(ttk.Frame):
    @classmethod
    def lookup(cls, search_type):
        form = ALL_FORMS[search_type]
        return lambda p, m: cls(p, form, m)

    def __init__(self, parent, search_form_cls, pharmacy):
        super().__init__(parent)
        self._form = search_form_cls(self, pharmacy)
        self._results = None

        self._form.grid(row=0, column=0, sticky="nsew")
        self._form.do_search.add_observer(self._show_results)

    def _show_results(self, search):
        self._clear_results()
        self._results = TableView(self, search)
        self._place_results()

    def _place_results(self):
        self._results.grid(row=1, column=0, sticky="nsew")

    def _clear_results(self):
        if self._results is not None:
            self._results.grid_forget()
            self._results.destroy()
            self._results = None

    def __on_search(self, search_type, params):
        self._show_results(
            getattr(self.pharmacy, search_type + "_search")(params))


class MultiSearchView(ttk.Frame):
    def __init__(self, parent, pharmacy):
        super().__init__(parent)
        self.pharmacy = pharmacy

        self._forms = {}
        for search_type, form_cls in ALL_FORMS.items():
            form = form_cls(self, pharmacy)
            form.do_search.add_observer(partial(self.do_search, search_type))
            self._forms[search_type] = form
        self._curform = None
        self._results = None

        self.form_selected.add_observer(self.__on_form_change)
        self.do_search.add_observer(self.__on_search)

        self._search_type = tk.StringVar()
        for i, search_type in enumerate(["patient",
                                         "doctor",
                                         "drug",
                                         "prescription"]):
            ttk.Radiobutton(self, text=search_type.title(),
                            command=self._switch_form,
                            variable=self._search_type, value=search_type) \
                .grid(row=0, column=i)
        self._search_type.set("patient")
        self._switch_form()

    @eventsource
    def do_search(search_type, params):
        pass

    @eventsource
    def form_selected(self):
        pass

    def _switch_form(self):
        search_type = self._search_type.get()
        self._clear_results()
        if self._curform:
            self._curform.grid_forget()

        self._curform = self._forms[search_type]
        self._curform.grid(row=1, column=0, columnspan=5)
        self.form_selected()

    def _place_results(self, tableview):
        self._clear_results()
        self._results = tableview
        self._results.grid(row=2, column=0, columnspan=5)

    def _clear_results(self):
        if self._results is not None:
            self._results.grid_forget()
            self._results.destroy()
            self._results = None

    def __on_form_change(self):
        self._clear_results()

    def __on_search(self, search_type, params):
        # TODO: move this into the form perhaps?
        search = getattr(self.pharmacy, search_type + "_search")(params)
        self._place_results(TableView(self, search))
