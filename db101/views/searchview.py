import tkinter as tk
from tkinter import ttk
from functools import partial

from ..observable import eventsource


class Spinbox(ttk.Entry):
    def __init__(self, master=None, **kw):
        super().__init__(master, "ttk::spinbox", **kw)

    def current(self, newindex=None):
        return self.tk.call(self._w, "current", newindex)

    def set(self, value):
        return self.tk.call(self._w, "set", value)


class DrugForm(ttk.Frame):
    ARGS = {"bigpharma", "formula", "sold", "price_min", "price_max"}

    def __init__(self, parent):
        super().__init__(parent)

        ttk.Label(self, text=" BigPharma ").grid(row=0, column=0)
        self.bigpharma = ttk.Entry(self)
        self.bigpharma.grid(row=0, column=1, columnspan=4)

        ttk.Label(self, text=" Formula ").grid(row=1, column=0)
        self.formula = ttk.Entry(self)
        self.formula.grid(row=1, column=1, columnspan=4)

        self.sold = tk.StringVar()
        ttk.Label(self, text=" Sold? ").grid(row=2, column=0)
        R1 = ttk.Radiobutton(self, text="Yes", variable=self.sold, value="yes")
        R2 = ttk.Radiobutton(self, text="No", variable=self.sold, value="no")
        R3 = ttk.Radiobutton(self, text="Don't care", variable=self.sold,
                             value="dont_care")

        R1.grid(row=2, column=1)
        R2.grid(row=2, column=2)
        R3.grid(row=2, column=3, columnspan=2)
        R1.invoke()

        ttk.Label(self, text="Price").grid(row=3, column=0)

        ttk.Label(self, text="min:").grid(row=3, column=1)
        self.price_min = Spinbox(self, from_=0, to=float("Inf"), width=3)
        self.price_min.grid(row=3, column=2)

        ttk.Label(self, text="max:").grid(row=3, column=3)
        self.price_max = Spinbox(self, from_=0, to=float("Inf"), width=3)
        self.price_max.grid(row=3, column=4)

        B1 = ttk.Button(self, text=" Search ", command=lambda: print(self.get()))
        B1.grid(row=4, column=5)

    def get(self):
        return {k: getattr(self, k).get() for k in self.ARGS}

    @eventsource
    def do_search(params):
        pass


class DoctorForm(ttk.Frame):
    ARGS = {"name", "specialty", "experience", "patient", "drug"}

    def __init__(self, parent):
        super().__init__(parent)

        ttk.Label(self, text=" Name ").grid(row=0, column=0)
        self.name = ttk.Entry(self)
        self.name.grid(row=0, column=1)

        ttk.Label(self, text=" Specialty ").grid(row=1, column=0)
        self.specialty = ttk.Entry(self)
        self.specialty.grid(row=1, column=1)

        ttk.Label(self, text=" Experience ").grid(row=2, column=0)
        self.experience = Spinbox(self, from_=0, to=float("Inf"), width=2)
        self.experience.grid(row=2, column=1)

        ttk.Label(self, text=" Patient ").grid(row=3, column=0)
        self.patient = ttk.Entry(self)
        self.patient.grid(row=3, column=1)

        ttk.Label(self, text=" Drug ").grid(row=4, column=0)
        self.drug = ttk.Entry(self)
        self.drug.grid(row=4, column=1)

        B1 = ttk.Button(self, text=" Search ", command=lambda: print(self.get()))
        B1.grid(row=5, column=3)

    def get(self):
        return {k: getattr(self, k).get() for k in self.ARGS}

    @eventsource
    def do_search(params):
        pass


class PatientForm(ttk.Frame):
    ARGS = {"name", "age_min", "age_max", "address", "drug"}

    def __init__(self, parent):
        super().__init__(parent)

        ttk.Label(self, text=" Name ").grid(row=0, column=0)
        self.name = ttk.Entry(self)
        self.name.grid(row=0, column=1, columnspan=4)

        ttk.Label(self, text=" Age ").grid(row=1, column=0)

        ttk.Label(self, text="min:").grid(row=1, column=1)
        self.age_min = Spinbox(self, from_=0, to=float("Inf"), width=2)
        self.age_min.grid(row=1, column=2)

        ttk.Label(self, text="max:").grid(row=1, column=3)
        self.age_max = Spinbox(self, from_=0, to=float("Inf"), width=2)
        self.age_max.grid(row=1, column=4)

        ttk.Label(self, text=" Address ").grid(row=2, column=0)
        self.address = ttk.Entry(self)
        self.address.grid(row=2, column=1, columnspan=4)

        ttk.Label(self, text=" Doctor ").grid(row=3, column=0)
        self.doctor = ttk.Entry(self)
        self.doctor.grid(row=3, column=1, columnspan=4)

        ttk.Label(self, text=" Drug ").grid(row=4, column=0)
        self.drug = ttk.Entry(self)
        self.drug.grid(row=4, column=1, columnspan=4)

        B1 = ttk.Button(self, text=" Search ", command=lambda: print(self.get()))
        B1.grid(row=5, column=5)

    def get(self):
        return {k: getattr(self, k).get() for k in self.ARGS}

    @eventsource
    def do_search(params):
        pass


class BigPharmaForm(ttk.Frame):
    ARGS = {"name", "phone", "drug", "contract_start", "contract_end"}

    def __init__(self, parent):
        super().__init__(parent)

        ttk.Label(self, text=" Name ").grid(row=0, column=0)
        self.name = ttk.Entry(self)
        self.name.grid(row=0, column=1)

        ttk.Label(self, text=" Phone ").grid(row=1, column=0)
        self.phone = ttk.Entry(self)
        self.phone.grid(row=1, column=1)

        ttk.Label(self, text=" Drug ").grid(row=2, column=0)
        self.drug = ttk.Entry(self)
        self.drug.grid(row=2, column=1)

        ttk.Label(self, text=" Contract Start ").grid(row=3, column=0)
        self.contract_start = ttk.Entry(self)
        self.contract_start.grid(row=3, column=1)

        ttk.Label(self, text=" Contract End ").grid(row=4, column=0)
        self.contract_end = ttk.Entry(self)
        self.contract_end.grid(row=4, column=1)

        B1 = ttk.Button(self, text=" Search ", command=lambda: print(self.get()))
        B1.grid(row=5, column=3)

    def get(self):
        return {k: getattr(self, k).get() for k in self.ARGS}

    @eventsource
    def do_search(params):
        pass


class PrescriptionForm(ttk.Frame):
    ARGS = {"doctor", "patient", "date", "drug"}

    def __init__(self, parent):
        super().__init__(parent)

        ttk.Label(self, text=" Doctor ").grid(row=0, column=0)
        self.doctor = ttk.Entry(self)
        self.doctor.grid(row=0, column=1)

        ttk.Label(self, text=" Patient ").grid(row=1, column=0)
        self.patient = ttk.Entry(self)
        self.patient.grid(row=1, column=1)

        ttk.Label(self, text=" Date ").grid(row=2, column=0)
        self.date = ttk.Entry(self)
        self.date.grid(row=2, column=1)

        ttk.Label(self, text=" Drug ").grid(row=3, column=0)
        self.drug = ttk.Entry(self)
        self.drug.grid(row=3, column=1)

        B1 = ttk.Button(self, text=" Search ", command=lambda: print(self.get()))
        B1.grid(row=4, column=3)

    def get(self):
        return {k: getattr(self, k).get() for k in self.ARGS}

    @eventsource
    def do_search(params):
        pass


class SearchView(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.curform = None
        self.drug_form = DrugForm(self)
        self.doctor_form = DoctorForm(self)
        self.patient_form = PatientForm(self)
        self.bigpharma_form = BigPharmaForm(self)
        self.prescription_form = PrescriptionForm(self)

        self.drug_form.do_search.add_observer(
            partial(self.do_search, "drug"))
        self.doctor_form.do_search.add_observer(
            partial(self.do_search, "doctor"))
        self.patient_form.do_search.add_observer(
            partial(self.do_search, "patient"))
        self.bigpharma_form.do_search.add_observer(
            partial(self.do_search, "bigpharma"))
        self.prescription_form.do_search.add_observer(
            partial(self.do_search, "prescription"))

        R1 = ttk.Radiobutton(self, text="Doctor", value=1,
                             command=self._switch_to(self.doctor_form))
        R1.grid(row=0, column=0)

        R2 = ttk.Radiobutton(self, text="Patient", value=2,
                             command=self._switch_to(self.patient_form))
        R2.grid(row=0, column=1)

        R3 = ttk.Radiobutton(self, text="Drug", value=3,
                             command=self._switch_to(self.drug_form))
        R3.grid(row=0, column=2)

        R4 = ttk.Radiobutton(self, text="BigPharma", value=4,
                             command=self._switch_to(self.bigpharma_form))
        R4.grid(row=0, column=3)

        R5 = ttk.Radiobutton(self, text="Prescription", value=5,
                             command=self._switch_to(self.prescription_form))
        R5.grid(row=0, column=4)

        R1.invoke()

        ttk.Frame(self).grid(row=2, column=0, columnspan=5)

    def _switch_to(self, new_form):
        def inner():
            if self.curform:
                self.curform.grid_forget()
            new_form.grid(row=1, column=0, columnspan=5)
            self.curform = new_form
        return inner

    @eventsource
    def do_search(search_type, params):
        pass
