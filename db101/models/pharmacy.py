from .model import Model


class Pharmacy(Model):
    def __init__(self, pharmacy_id, mapper):
        super().__init__(mapper, {
            "our_pharmacy": pharmacy_id,
        })

    # @eventsource
    # def changed():
    #     pass


class DrugsOnSale(Pharmacy.Query):
    ARGUMENTS = {
        "our_pharmacy": int
    }
    RETURNS = ("name", "maker", "formula", "price")


class CountDrugsOnSale(Pharmacy.Query):
    ARGUMENTS = {
        "our_pharmacy": int
    }
    RETURNS = ("count")


class PatientSearch(Pharmacy.Query):
    ARGUMENTS = {
        "our_pharmacy": int,
        "name": str,
        "age_min": int,
        "age_max": int,
        "doctor": str,
        "address": str,
        "drug": str
    }
    RETURNS = ("name", "age", "address", "doctor")


class DoctorSearch(Pharmacy.Query):
    ARGUMENTS = {
        "our_pharmacy": int,
        "name": str,
        "specialty": str,
        "exp": int,
        "patient": str,
        "drug": str
    }
    RETURNS = ("name", "specialty", "exp")
