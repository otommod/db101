import tkinter as tk
from tkinter import ttk


class Spinbox(ttk.Entry):
    def __init__(self, master=None, **kw):
        super().__init__(master, "ttk::spinbox", **kw)

    def current(self, newindex=None):
        return self.tk.call(self._w, "current", newindex)

    def set(self, value):
        return self.tk.call(self._w, "set", value)


class DrugForm(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        ttk.Label(self, text=" BigPharma ").grid(row=0, column=0)
        self.bigpharma = ttk.Entry(self, bd=2)
        self.bigpharma.grid(row=0, column=1, columnspan=4)

        ttk.Label(self, text=" Formula ").grid(row=1, column=0)
        self.formula = ttk.Entry(self, bd=2)
        self.formula.grid(row=1, column=1, columnspan=4)

        self.sold = tk.IntVar()
        ttk.Label(self, text=" Sold? ").grid(row=2, column=0)
        R1 = ttk.Radiobutton(self, text="Yes ", variable=self.sold, value=1)
        R2 = ttk.Radiobutton(self, text="No", variable=self.sold, value=2)
        R3 = ttk.Radiobutton(self, text="Don't care", variable=self.sold, value=3)

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
        return (self.bigpharma.get(),
                self.formula.get(),
                self.sold.get(),
                self.price_min.get(),
                self.price_max.get())


class DoctorForm(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        ttk.Label(self, text=" Name ").grid(row=0, column=0)
        self.name = ttk.Entry(self, bd=2)
        self.name.grid(row=0, column=1)

        ttk.Label(self, text=" Specialty ").grid(row=1, column=0)
        self.specialty = ttk.Entry(self, bd=2)
        self.specialty.grid(row=1, column=1)

        ttk.Label(self, text=" Experience ").grid(row=2, column=0)
        self.experience = Spinbox(self, from_=0, to=float("Inf"), width=2)
        self.experience.grid(row=2, column=1)

        ttk.Label(self, text=" Patient ").grid(row=3, column=0)
        self.patient = ttk.Entry(self, bd=2)
        self.patient.grid(row=3, column=1)

        ttk.Label(self, text=" Drug ").grid(row=4, column=0)
        self.drug = ttk.Entry(self, bd=2)
        self.drug.grid(row=4, column=1)

        B1 = ttk.Button(self, text=" Search ", command=lambda: print(self.get()))
        B1.grid(row=5, column=3)

    def get(self):
        return (self.name.get(),
                self.specialty.get(),
                self.experience.get(),
                self.patient.get(),
                self.drug.get())


class PatientForm(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        ttk.Label(self, text=" Name ").grid(row=0, column=0)
        self.name = ttk.Entry(self, bd=2)
        self.name.grid(row=0, column=1, columnspan=4)

        ttk.Label(self, text=" Age ").grid(row=1, column=0)

        ttk.Label(self, text="min:").grid(row=1, column=1)
        self.age_min = Spinbox(self, from_=0, to=float("Inf"), width=2)
        self.age_min.grid(row=1, column=2)

        ttk.Label(self, text="max:").grid(row=1, column=3)
        self.age_max = .Spinbox(self, from_=0, to=float("Inf"), width=2)
        self.age_max.grid(row=1, column=4)

        ttk.Label(self, text=" Adress ").grid(row=2, column=0)
        self.adress = ttk.Entry(self, bd=2)
        self.adress.grid(row=2, column=1, columnspan=4)

        ttk.Label(self, text=" Doctor ").grid(row=3, column=0)
        self.doctor = ttk.Entry(self, bd=2)
        self.doctor.grid(row=3, column=1, columnspan=4)

        ttk.Label(self, text=" Drug ").grid(row=4, column=0)
        self.drug = ttk.Entry(self, bd=2)
        self.drug.grid(row=4, column=1, columnspan=4)

        B1 = ttk.Button(self, text=" Search ", command=lambda: print(self.get()))
        B1.grid(row=5, column=5)

    def get(self):
        return (self.name.get(),
                self.age_min.get(),
                self.age_max.get(),
                self.adress.get(),
                self.doctor.get(),
                self.drug.get())


class BigPharmaForm(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        ttk.Label(self, text=" Name ").grid(row=0, column=0)
        self.name = ttk.Entry(self, bd=2)
        self.name.grid(row=0, column=1)

        ttk.Label(self, text=" Phone ").grid(row=1, column=0)
        self.phone = ttk.Entry(self, bd=2)
        self.phone.grid(row=1, column=1)

        ttk.Label(self, text=" Drug ").grid(row=2, column=0)
        self.drug = ttk.Entry(self, bd=2)
        self.drug.grid(row=2, column=1)

        ttk.Label(self, text=" Contract Start ").grid(row=3, column=0)
        self.contract_start = ttk.Entry(self, bd=2)
        self.contract_start.grid(row=3, column=1)

        ttk.Label(self, text=" Contract End ").grid(row=4, column=0)
        self.contract_end = ttk.Entry(self, bd=2)
        self.contract_end.grid(row=4, column=1)

        B1 = ttk.Button(self, text=" Search ", command=lambda: print(self.get()))
        B1.grid(row=5, column=3)

    def get(self):
        return (self.name.get(),
                self.phone.get(),
                self.drug.get(),
                self.contract_start.get(),
                self.contract_end.get())


class PrescriptionForm(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        ttk.Label(self, text=" Doctor ").grid(row=0, column=0)
        self.doctor = ttk.Entry(self, bd=2)
        self.doctor.grid(row=0, column=1)

        ttk.Label(self, text=" Patient ").grid(row=1, column=0)
        self.patient = ttk.Entry(self, bd=2)
        self.patient.grid(row=1, column=1)

        ttk.Label(self, text=" Date ").grid(row=2, column=0)
        self.date = ttk.Entry(self, bd=2)
        self.date.grid(row=2, column=1)

        ttk.Label(self, text=" Drug ").grid(row=3, column=0)
        self.drug = ttk.Entry(self, bd=2)
        self.drug.grid(row=3, column=1)

        B1 = ttk.Button(self, text=" Search ", command=lambda: print(self.get()))
        B1.grid(row=4, column=3)

    def get(self):
        return (self.doctor.get(),
                self.patient.get(),
                self.date.get(),
                self.drug.get())


class SearchForm(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.drug_form = DrugForm(self)
        self.doctor_form = DoctorForm(self)
        self.patient_form = PatientForm(self)
        self.bigpharma_form = BigPharmaForm(self)
        self.prescription_form = PrescriptionForm(self)
        self.curform = None

        R1 = ttk.Radiobutton(self, text="Doctor",
                             command=self._switch_to(self.doctor_form),value = '1')
        R1.grid(row=0, column=0)

        R2 = ttk.Radiobutton(self, text="Patient",
                             command=self._switch_to(self.patient_form),value = '2')
        R2.grid(row=0, column=1)

        R3 = ttk.Radiobutton(self, text="Drug",
                             command=self._switch_to(self.drug_form),value = '3')
        R3.grid(row=0, column=2)

        R4 = ttk.Radiobutton(self, text="BigPharma",
                             command=self._switch_to(self.bigpharma_form),value = '4')
        R4.grid(row=0, column=3)

        R5 = ttk.Radiobutton(self, text="Prescription",
                             command=self._switch_to(self.prescription_form),value = '5')
        R5.grid(row=0, column=4)

        # R1.invoke()

    def _switch_to(self, new_form):
        def inner():
            if self.curform:
                self.curform.grid_forget()
            new_form.grid(row=1, column=0,columnspan=5)
            self.curform = new_form
        return inner


root = tk.Tk()

searchform = SearchForm(root)
searchform.grid()

root.mainloop()
