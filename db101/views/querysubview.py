import tkinter as tk
from tkinter import ttk
from . import TableView


class QuerySubView(ttk.Frame):
    @classmethod
    def lookup(cls, query, *args, **kwargs):
        return {
            "Total patient count": TotalPatientCount,
            "The Doctors and their patients": DoctorsAndPatients,
            "Number of pharmacies selling each drug": CountPharmaciesByDrug,
            "The drugs of patient...": DrugsOfPatient,
            "The drugs that older people use": DrugsForOldPatients,
            "The doctors of old patients": DoctorsOfOldPatients,

            "Our customers": OurCustomers,
            "How many drugs do we sell?": HowManyDrugsWeSell,
            "What drugs do we sell?": DrugsWeSell,
            "What drugs could we sell?": PotentialDrugs,
            "Contracts closest due": ContractsOrdered,
            "Contracts that end before...": ContractsBefore,
            "Partnered Pharmaceuticals": PartneredBigpharmas,
            "Not partnered Pharmaceuticals": NotPartneredBigpharmas,
            "Potential future partners": DrugsOtherPharmasSell,
        }[query]


class TotalPatientCount(QuerySubView):
    def __init__(self, parent, general):
        super().__init__(parent)
        self.label = ttk.Label(self)
        self.count = general.count_patients()

        self.label.grid()
        self.render()

    def render(self):
        number = self.count.get()[0][0]
        self.label.configure(text="There are %s patients in total" % str(number))


class DoctorsOfOldPatients(QuerySubView):
    def __init__(self, parent, general):
        super().__init__(parent)
        doctors = general.doctors_with_old_patients()
        self.table = TableView(self, doctors)
        self.table.grid()


class CountPharmaciesByDrug(QuerySubView):
    def __init__(self, parent, general):
        super().__init__(parent)
        self.general = general
        self.counts = self.general.count_pharmacies_by_drug()

        self.table = TableView(self, self.counts)
        self.table.grid(in_=self)


class DoctorsAndPatients(QuerySubView):
    def __init__(self, parent, general):
        super().__init__(parent)
        self.general = general
        self.people = self.general.patients_and_doctors()

        self.table = TableView(self, self.people)
        self.table.grid(in_=self)


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
        number = self.count.get()[0][0]
        self.label.configure(text=str(number))


class DrugsWeSell(QuerySubView):
    def __init__(self, parent, pharmacy):
        super().__init__(parent)
        drugs = pharmacy.drugs_on_sale()
        self.table = TableView(self, drugs)
        self.table.grid()


class PotentialDrugs(QuerySubView):
    def __init__(self, parent, pharmacy):
        super().__init__(parent)
        self.pharmacy = pharmacy
        self.drugs = pharmacy.potential_drugs()
        self.table = TableView(self, self.drugs)

        ttk.Label(self, text=("These are the drugs from our partnered"
                              " companies that we do not sell")).grid()
        self.table.grid()


class ContractsBefore(QuerySubView):
    def __init__(self, parent, pharmacy):
        super().__init__(parent)
        self.pharmacy = pharmacy

        self.label = ttk.Label(self, text="There are ___ contracts that")
        self.label.grid(columnspan=2)

        self.date_type = tk.StringVar()
        ttk.Radiobutton(self, text="end before", variable=self.date_type,
                        value="end").grid(row=1, column=0)
        ttk.Radiobutton(self, text="start after", variable=self.date_type,
                        value="start").grid(row=1, column=1)

        self.date = ttk.Entry(self)
        self.date.grid(columnspan=2)

        self.date.bind("<Return>", self.render)

    def render(self, event):
        contracts = self.pharmacy.count_contracts_by_date({
            "date_type": self.date_type.get(),
            "date": self.date.get()
        }).get()[0][0]
        self.label.configure(
            text="There are %s contracts that end before" % contracts)


class ContractsOrdered(QuerySubView):
    def __init__(self, parent, pharmacy):
        super().__init__(parent)
        self.pharmacy = pharmacy
        self.contracts = self.pharmacy.contracts_due()

        # ttk.Label(self, text=("These are our contracts, starting with the "
        #                       "first due")).grid()
        self.table = TableView(self, self.contracts)
        self.table.grid()


class PartneredBigpharmas(QuerySubView):
    def __init__(self, parent, pharmacy):
        super().__init__(parent)
        self.pharmacy = pharmacy
        self.partners = self.pharmacy.partnered_bigpharmas()

        self.table = TableView(self, self.partners)
        self.table.grid()


class NotPartneredBigpharmas(QuerySubView):
    def __init__(self, parent, pharmacy):
        super().__init__(parent)
        self.pharmacy = pharmacy
        self.partners = self.pharmacy.not_partnered_bigpharmas()

        self.table = TableView(self, self.partners)
        self.table.grid()


class DrugsOfPatient(QuerySubView):
    def __init__(self, parent, general):
        super().__init__(parent)
        self.general = general
        self.name = ttk.Entry(self, width=20)
        self.table = None

        ttk.Label(self, text="Patient").grid(sticky="e")
        self.name.grid(row=0, column=1, sticky="ew")
        ttk.Label(self, text="is on...").grid(row=0, column=2, sticky="w")

        self.name.bind("<Return>", self.render)

    def render(self, event):
        drugs = self.general.drugs_of_patient({"name": self.name.get()})
        if self.table is not None:
            self.table.grid_forget()
            self.table.destroy()
        self.table = TableView(self, drugs)
        self.table.grid(row=1, column=0, columnspan=3, sticky="nsew")


class DrugsForOldPatients(QuerySubView):
    def __init__(self, parent, general):
        super().__init__(parent)
        self.general = general
        self.old_people_drugs = self.general.drugs_for_old_patients()

        self.table = TableView(self, self.old_people_drugs)
        self.table.grid()


class DrugsOtherPharmasSell(QuerySubView):
    def __init__(self, parent, pharmacy):
        super().__init__(parent)
        other_drugs = pharmacy.drugs_from_other_pharmas()
        self.table = TableView(self, other_drugs)
        self.table.grid()


class OurCustomers(QuerySubView):
    def __init__(self, parent, pharmacy):
        super().__init__(parent)
        customers = pharmacy.patients_prescriptions()
        self.table = TableView(self, customers)
        self.table.grid()
