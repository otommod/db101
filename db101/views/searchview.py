import tkinter as tk
from tkinter import ttk
from functools import partial

from . import TableView
from ..observable import eventsource


class Spinbox(ttk.Entry):
    def __init__(self, master=None, **kw):
        super().__init__(master, "ttk::spinbox", **kw)

    def current(self, newindex=None):
        return self.tk.call(self._w, "current", newindex)

    def set(self, value):
        return self.tk.call(self._w, "set", value)


class SearchForm(ttk.Frame):
    def __init__(self, parent, query):
        super().__init__(parent)
        self.query = query
        self.tableview = None

        self.do_search.add_observer(self._add_search_results)

    @eventsource
    def do_search(params):
        pass

    def get(self):
        results = {k: v for k in self.ARGS
                   for v in [getattr(self, k).get()] if v}
        return results

    def _add_search_results(self, params):
        if self.tableview is not None:
            self.tableview.grid_forget()
            self.tableview.destroy()

        self.tableview = TableView(self, self.query(params))
        self.tableview.grid(row=6, column=1)


class DrugSearchView(SearchForm):
    ARGS = {"bigpharma", "formula", "sold", "price_min", "price_max"}

    def __init__(self, parent, model):
        super().__init__(parent, model.drug_search)

        ttk.Label(self, text=" BigPharma ").grid(row=0, column=0)
        self.bigpharma = ttk.Entry(self)
        self.bigpharma.grid(row=0, column=1, columnspan=4)

        ttk.Label(self, text=" Formula ").grid(row=1, column=0)
        self.formula = ttk.Entry(self)
        self.formula.grid(row=1, column=1, columnspan=4)

        self.sold = tk.StringVar()
        ttk.Label(self, text=" Sold? ").grid(row=2, column=0)
        ttk.Radiobutton(self, text="Yes",
                        variable=self.sold, value="yes").grid(row=2, column=1)
        ttk.Radiobutton(self, text="No",
                        variable=self.sold, value="no").grid(row=2, column=2)
        r = ttk.Radiobutton(self, variable=self.sold, value="dont_care",
                            text="Don't care")
        r.grid(row=2, column=3, columnspan=2)
        r.invoke()

        ttk.Label(self, text="Price").grid(row=3, column=0)

        ttk.Label(self, text="min:").grid(row=3, column=1)
        self.price_min = Spinbox(self, from_=0, to=float("Inf"), width=4)
        self.price_min.grid(row=3, column=2)

        ttk.Label(self, text="max:").grid(row=3, column=3)
        self.price_max = Spinbox(self, from_=0, to=float("Inf"), width=4)
        self.price_max.grid(row=3, column=4)

        ttk.Button(self, text="Search",
                   command=lambda: self.do_search(self.get())) \
            .grid(row=4, column=5)


class DoctorSearchView(SearchForm):
    ARGS = {"name", "specialty", "exp", "patient", "drug"}

    def __init__(self, parent, model):
        super().__init__(parent, model.doctor_search)

        ttk.Label(self, text="Doctor Name").grid(row=0, column=0)
        self.name = ttk.Entry(self)
        self.name.grid(row=0, column=1)

        ttk.Label(self, text="Specialty").grid(row=1, column=0)
        self.specialty = ttk.Entry(self)
        self.specialty.grid(row=1, column=1)

        ttk.Label(self, text="Experience").grid(row=2, column=0)
        self.exp = Spinbox(self, from_=0, to=float("Inf"), width=3)
        self.exp.grid(row=2, column=1)

        ttk.Label(self, text="Patient Name").grid(row=3, column=0)
        self.patient = ttk.Entry(self)
        self.patient.grid(row=3, column=1)

        ttk.Label(self, text="Drug").grid(row=4, column=0)
        self.drug = ttk.Entry(self)
        self.drug.grid(row=4, column=1)

        ttk.Button(self, text="Search",
                   command=lambda: self.do_search(self.get())) \
            .grid(row=5, column=3)


class PatientSearchView(SearchForm):
    ARGS = {"name", "doctor", "age_min", "age_max", "address", "drug"}

    def __init__(self, parent, model):
        super().__init__(parent, model.patient_search)

        ttk.Label(self, text="Name").grid(row=0, column=0)
        self.name = ttk.Entry(self)
        self.name.grid(row=0, column=1, columnspan=4)

        ttk.Label(self, text="Age").grid(row=1, column=0)

        ttk.Label(self, text="min:").grid(row=1, column=1)
        self.age_min = Spinbox(self, from_=0, to=float("Inf"), width=3)
        self.age_min.grid(row=1, column=2)

        ttk.Label(self, text="max:").grid(row=1, column=3)
        self.age_max = Spinbox(self, from_=0, to=float("Inf"), width=3)
        self.age_max.grid(row=1, column=4)

        ttk.Label(self, text="Address").grid(row=2, column=0)
        self.address = ttk.Entry(self)
        self.address.grid(row=2, column=1, columnspan=4)

        ttk.Label(self, text="Doctor").grid(row=3, column=0)
        self.doctor = ttk.Entry(self)
        self.doctor.grid(row=3, column=1, columnspan=4)

        ttk.Label(self, text="Drug").grid(row=4, column=0)
        self.drug = ttk.Entry(self)
        self.drug.grid(row=4, column=1, columnspan=4)

        ttk.Button(self, text="Search",
                   command=lambda: self.do_search(self.get())) \
            .grid(row=5, column=5)


class BigPharmaSearchView(SearchForm):
    ARGS = {"name", "phone", "drug", "contract_start", "contract_end"}

    def __init__(self, parent, model):
        super().__init__(parent, model.bigpharma_search)

        ttk.Label(self, text="Name").grid(row=0, column=0)
        self.name = ttk.Entry(self)
        self.name.grid(row=0, column=1)

        ttk.Label(self, text="Phone").grid(row=1, column=0)
        self.phone = ttk.Entry(self)
        self.phone.grid(row=1, column=1)

        ttk.Label(self, text="Drug").grid(row=2, column=0)
        self.drug = ttk.Entry(self)
        self.drug.grid(row=2, column=1)

        ttk.Label(self, text="Contract Start").grid(row=3, column=0)
        self.contract_start = ttk.Entry(self)
        self.contract_start.grid(row=3, column=1)

        ttk.Label(self, text="Contract End").grid(row=4, column=0)
        self.contract_end = ttk.Entry(self)
        self.contract_end.grid(row=4, column=1)

        ttk.Button(self, text="Search",
                   command=lambda: self.do_search(self.get())) \
            .grid(row=5, column=3)


class PrescriptionSearchView(SearchForm):
    ARGS = {"doctor", "patient", "date", "drug"}

    def __init__(self, parent, model):
        super().__init__(parent, model.prescription_search)

        ttk.Label(self, text="Doctor").grid(row=0, column=0, stick="e")
        self.doctor = ttk.Entry(self)
        self.doctor.grid(row=0, column=1)

        ttk.Label(self, text="Patient").grid(row=1, column=0, stick="e")
        self.patient = ttk.Entry(self)
        self.patient.grid(row=1, column=1)

        ttk.Label(self, text="Date").grid(row=2, column=0, stick="e")
        self.date = ttk.Entry(self)
        self.date.grid(row=2, column=1)

        ttk.Label(self, text="Drug").grid(row=3, column=0, stick="e")
        self.drug = ttk.Entry(self)
        self.drug.grid(row=3, column=1)

        ttk.Button(self, text="Search",
                   command=lambda: self.do_search(self.get())) \
            .grid(row=4, column=3)


class MultiSearchView(ttk.Frame):
    ALL_FORMS = {
        "drug": DrugSearchView,
        "doctor": DoctorSearchView,
        "patient": PatientSearchView,
        "bigpharma": BigPharmaSearchView,
        "prescription": PrescriptionSearchView,
    }

    @classmethod
    def lookup(cls, search_type):
        return cls.ALL_FORMS[search_type]

    def __init__(self, parent, model):
        super().__init__(parent)
        self.model = model

        self._curform = None
        self._forms = {k: v(self, model) for k, v in self.ALL_FORMS.items()}
        for k, v in self._forms.items():
            v.do_search.add_observer(partial(self.do_search, k))

        self._search_type = tk.StringVar()
        r = ttk.Radiobutton(self, text="Patient", command=self._switch_form,
                            variable=self._search_type, value="patient")
        r.grid(row=0, column=0)

        ttk.Radiobutton(self, text="Doctor", command=self._switch_form,
                        variable=self._search_type, value="doctor") \
            .grid(row=0, column=1)

        ttk.Radiobutton(self, text="Drug", command=self._switch_form,
                        variable=self._search_type, value="drug") \
            .grid(row=0, column=2)

        ttk.Radiobutton(self, text="BigPharma", command=self._switch_form,
                        variable=self._search_type, value="bigpharma") \
            .grid(row=0, column=3)

        ttk.Radiobutton(self, text="Prescription", command=self._switch_form,
                        variable=self._search_type, value="prescription") \
            .grid(row=0, column=4)

        r.invoke()

    def _switch_form(self):
        search_type = self._search_type.get()
        if self._curform:
            self._curform.grid_forget()

        self._curform = self._forms[search_type]
        self._curform.grid(row=1, column=0, columnspan=5)
        self.form_selected()

    @eventsource
    def do_search(search_type, params):
        pass

    @eventsource
    def form_selected(self):
        pass
