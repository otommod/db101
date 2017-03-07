import tkinter as tk
from tkinter import ttk


class DrugForm(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        L1 = ttk.Label(self, text=" BigPharma ")
        L1.grid(row=0, column=0)

        self.bigpharma = tk.Entry(self, bd=2)
        self.bigpharma.grid(row=0, column=1, columnspan=4)

        L2 = ttk.Label(self, text=" Formula ")
        L2.grid(row=1, column=0)

        self.formula = tk.Entry(self, bd=2)
        self.formula.grid(row=1, column=1, columnspan=4)

        L3 = ttk.Label(self, text=" Sold? ")
        L3.grid(row=2, column=0)

        self.sold = tk.IntVar()
        R1 = ttk.Radiobutton(self, text="Yes ", variable=self.sold, value=1)
        R1.grid(row=2, column=1)

        R2 = ttk.Radiobutton(self, text="No ", variable=self.sold, value=2)
        R2.grid(row=2, column=2)

        R3 = ttk.Radiobutton(self, text="I don't know ", variable=self.sold, value=3)
        R3.grid(row=2, column=3, columnspan=2)

        L4 = ttk.Label(self, text=" Price ")
        L4.grid(row=3, column=0)

        L5 = ttk.Label(self, text="min:")
        L5.grid(row=3, column=1)

        self.price_min = tk.Spinbox(self, from_=0, to=float("Inf"), width=3)
        self.price_min.grid(row=3, column=2)

        L6 = ttk.Label(self, text="max:")
        L6.grid(row=3, column=3)

        self.price_max = tk.Spinbox(self, from_=0, to=float("Inf"), width=3)
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

        L1 = ttk.Label(self, text=" Name ")
        L1.grid(row=0, column=0)

        self.name = tk.Entry(self, bd=2)
        self.name.grid(row=0, column=1)

        L2 = ttk.Label(self, text=" Specialty ")
        L2.grid(row=1, column=0)

        self.specialty = tk.Entry(self, bd=2)
        self.specialty.grid(row=1, column=1)

        L3 = ttk.Label(self, text=" Experience ")
        L3.grid(row=2, column=0)

        self.experience = tk.Spinbox(self, from_=0, to=float("Inf"), width=2)
        self.experience.grid(row=2, column=1)

        L4 = ttk.Label(self, text=" Patient ")
        L4.grid(row=3, column=0)

        self.patient = tk.Entry(self, bd=2)
        self.patient.grid(row=3, column=1)

        L5 = ttk.Label(self, text=" Drug ")
        L5.grid(row=4, column=0)

        self.drug = tk.Entry(self, bd=2)
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

        L1 = ttk.Label(self, text=" Name ")
        L1.grid(row=0, column=0)

        self.name = tk.Entry(self, bd=2)
        self.name.grid(row=0, column=1, columnspan=4)

        L2 = ttk.Label(self, text=" Age ")
        L2.grid(row=1, column=0)

        L3 = ttk.Label(self, text="min:")
        L3.grid(row=1, column=1)

        self.age_min = tk.Spinbox(self, from_=0, to=float("Inf"), width=2)
        self.age_min.grid(row=1, column=2)

        L4 = ttk.Label(self, text="max:")
        L4.grid(row=1, column=3)

        self.age_max = tk.Spinbox(self, from_=0, to=float("Inf"), width=2)
        self.age_max.grid(row=1, column=4)

        L4 = ttk.Label(self, text=" Adress ")
        L4.grid(row=2, column=0)

        self.adress = tk.Entry(self, bd=2)
        self.adress.grid(row=2, column=1, columnspan=4)

        L5 = ttk.Label(self, text=" Doctor ")
        L5.grid(row=3, column=0)

        self.doctor = tk.Entry(self, bd=2)
        self.doctor.grid(row=3, column=1, columnspan=4)

        L6 = ttk.Label(self, text=" Drug ")
        L6.grid(row=4, column=0)

        self.drug = tk.Entry(self, bd=2)
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

        L1 = ttk.Label(self, text=" Name ")
        L1.grid(row=0, column=0)

        self.name = tk.Entry(self, bd=2)
        self.name.grid(row=0, column=1)

        L2 = ttk.Label(self, text=" Phone ")
        L2.grid(row=1, column=0)

        self.phone = tk.Entry(self, bd=2)
        self.phone.grid(row=1, column=1)

        L3 = ttk.Label(self, text=" Drug ")
        L3.grid(row=2, column=0)

        self.drug = tk.Entry(self, bd=2)
        self.drug.grid(row=2, column=1)

        L4 = ttk.Label(self, text=" Contract Start ")
        L4.grid(row=3, column=0)

        self.contract_start = tk.Entry(self, bd=2)
        self.contract_start.grid(row=3, column=1)

        L5 = ttk.Label(self, text=" Contract End ")
        L5.grid(row=4, column=0)

        self.contract_end = tk.Entry(self, bd=2)
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

        L1 = ttk.Label(self, text=" Doctor ")
        L1.grid(row=0, column=0)

        self.doctor = tk.Entry(self, bd=2)
        self.doctor.grid(row=0, column=1)

        L2 = ttk.Label(self, text=" Patient ")
        L2.grid(row=1, column=0)

        self.patient = tk.Entry(self, bd=2)
        self.patient.grid(row=1, column=1)

        L3 = ttk.Label(self, text=" Date ")
        L3.grid(row=2, column=0)

        self.date = tk.Entry(self, bd=2)
        self.date.grid(row=2, column=1)

        L4 = ttk.Label(self, text=" Drug ")
        L4.grid(row=3, column=0)

        self.drug = tk.Entry(self, bd=2)
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
