import tkinter as tk
from tkinter import ttk


class DrugForm(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        L1 = ttk.Label(self, text=" BigPharma ")
        L1.grid(row=0, column=0)

        E1 = tk.Entry(self, bd=2)
        E1.grid(row=0, column=1, columnspan=4)

        L2 = ttk.Label(self, text=" Formula ")
        L2.grid(row=1, column=0)

        E2 = tk.Entry(self, bd=2)
        E2.grid(row=1, column=1, columnspan=4)

        L3 = ttk.Label(self, text=" Sold? ")
        L3.grid(row=2, column=0)

        C1 = ttk.Checkbutton(self, text="Yes ", onvalue=1, offvalue=0)
        C1.grid(row=2, column=1)

        C2 = ttk.Checkbutton(self, text="No ", onvalue=1, offvalue=0)
        C2.grid(row=2, column=2)

        C3 = ttk.Checkbutton(self, text="I don't know ", onvalue=1, offvalue=0)
        C3.grid(row=2, column=3, columnspan=2)

        L4 = ttk.Label(self, text=" Price ")
        L4.grid(row=3, column=0)

        L5 = ttk.Label(self, text="min:")
        L5.grid(row=3, column=1)

        S1 = tk.Spinbox(self, from_=0, to=float("Inf"), width=3)
        S1.grid(row=3, column=2)

        L6 = ttk.Label(self, text="max:")
        L6.grid(row=3, column=3)

        S2 = tk.Spinbox(self, from_=0, to=float("Inf"), width=3)
        S2.grid(row=3, column=4)

        B1 = ttk.Button(self, text=" Search ", command=exit)
        B1.grid(row=4, column=5)


class DoctorForm(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        L1 = ttk.Label(self, text=" Name ")
        L1.grid(row=0, column=0)

        E1 = tk.Entry(self, bd=2)
        E1.grid(row=0, column=1)

        L2 = ttk.Label(self, text=" Specialty ")
        L2.grid(row=1, column=0)

        E2 = tk.Entry(self, bd=2)
        E2.grid(row=1, column=1)

        L3 = ttk.Label(self, text=" Experience ")
        L3.grid(row=2, column=0)

        S1 = tk.Spinbox(self, from_=0, to=float("Inf"), width=2)
        S1.grid(row=2, column=1)

        L4 = ttk.Label(self, text=" Patient ")
        L4.grid(row=3, column=0)

        E3 = tk.Entry(self, bd=2)
        E3.grid(row=3, column=1)

        L5 = ttk.Label(self, text=" Drug ")
        L5.grid(row=4, column=0)

        E4 = tk.Entry(self, bd=2)
        E4.grid(row=4, column=1)

        B1 = ttk.Button(self, text=" Search ", command=exit)
        B1.grid(row=5, column=3)


class PatientForm(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        L1 = ttk.Label(self, text=" Name ")
        L1.grid(row=0, column=0)

        E1 = tk.Entry(self, bd=2)
        E1.grid(row=0, column=1, columnspan=4)

        L2 = ttk.Label(self, text=" Age ")
        L2.grid(row=1, column=0)

        L3 = ttk.Label(self, text="min:")
        L3.grid(row=1, column=1)

        S1 = tk.Spinbox(self, from_=0, to=float("Inf"), width=2)
        S1.grid(row=1, column=2)

        L4 = ttk.Label(self, text="max:")
        L4.grid(row=1, column=3)

        S2 = tk.Spinbox(self, from_=0, to=float("Inf"), width=2)
        S2.grid(row=1, column=4)

        L4 = ttk.Label(self, text=" Adress ")
        L4.grid(row=2, column=0)

        E2 = tk.Entry(self, bd=2)
        E2.grid(row=2, column=1, columnspan=4)

        L5 = ttk.Label(self, text=" Doctor ")
        L5.grid(row=3, column=0)

        E3 = tk.Entry(self, bd=2)
        E3.grid(row=3, column=1, columnspan=4)

        L6 = ttk.Label(self, text=" Drug ")
        L6.grid(row=4, column=0)

        E3 = tk.Entry(self, bd=2)
        E3.grid(row=4, column=1, columnspan=4)

        B1 = ttk.Button(self, text=" Search ", command=exit)
        B1.grid(row=5, column=5)


class BigPharmaForm(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        L1 = ttk.Label(self, text=" Name ")
        L1.grid(row=0, column=0)

        E1 = tk.Entry(self, bd=2)
        E1.grid(row=0, column=1)

        L2 = ttk.Label(self, text=" Phone ")
        L2.grid(row=1, column=0)

        E2 = tk.Entry(self, bd=2)
        E2.grid(row=1, column=1)

        L3 = ttk.Label(self, text=" Drug ")
        L3.grid(row=2, column=0)

        E3 = tk.Entry(self, bd=2)
        E3.grid(row=2, column=1)

        L4 = ttk.Label(self, text=" Contract Start ")
        L4.grid(row=3, column=0)

        E4 = tk.Entry(self, bd=2)
        E4.grid(row=3, column=1)

        L5 = ttk.Label(self, text=" Contract End ")
        L5.grid(row=4, column=0)

        E5 = tk.Entry(self, bd=2)
        E5.grid(row=4, column=1)

        B1 = ttk.Button(self, text=" Search ", command=exit)
        B1.grid(row=5, column=3)


class PrescriptionForm(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        L1 = ttk.Label(self, text=" Doctor ")
        L1.grid(row=0, column=0)

        E1 = tk.Entry(self, bd=2)
        E1.grid(row=0, column=1)

        L2 = ttk.Label(self, text=" Patient ")
        L2.grid(row=1, column=0)

        E2 = tk.Entry(self, bd=2)
        E2.grid(row=1, column=1)

        L3 = ttk.Label(self, text=" Date ")
        L3.grid(row=2, column=0)

        E3 = tk.Entry(self, bd=2)
        E3.grid(row=2, column=1)

        L4 = ttk.Label(self, text=" Drug ")
        L4.grid(row=3, column=0)

        E4 = tk.Entry(self, bd=2)
        E4.grid(row=3, column=1)

        B1 = ttk.Button(self, text=" Search ", command=exit)
        B1.grid(row=4, column=3)


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
                             command=self._switch_to(self.doctor_form))
        R1.grid(row=0, column=0)

        R2 = ttk.Radiobutton(self, text="Patient",
                             command=self._switch_to(self.patient_form))
        R2.grid(row=0, column=1)

        R3 = ttk.Radiobutton(self, text="Drug",
                             command=self._switch_to(self.drug_form))
        R3.grid(row=0, column=2)

        R4 = ttk.Radiobutton(self, text="BigPharma",
                             command=self._switch_to(self.bigpharma_form))
        R4.grid(row=0, column=3)

        R5 = ttk.Radiobutton(self, text="Prescription",
                             command=self._switch_to(self.prescription_form))
        R5.grid(row=0, column=4)

        # R1.invoke()

    def _switch_to(self, new_form):
        def inner():
            if self.curform:
                self.curform.grid_forget()
            new_form.grid(row=1, column=0)
            self.curform = new_form
        return inner


root = tk.Tk()

searchform = SearchForm(root)
searchform.grid()

root.mainloop()
