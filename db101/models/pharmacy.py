from .model import Model


class Pharmacy(Model):
    def __init__(self, pharmacy_id, mapper):
        super().__init__(mapper, {
            "our_pharmacy": pharmacy_id,
        })


class DrugsOnSale(Pharmacy.Query):
    ARGUMENTS = {
        "our_pharmacy": int
    }
    RETURNS = ("name", "maker", "formula", "price")

class CountDrugsOnSale(Pharmacy.Query):
    ARGUMENTS = {
        "our_pharmacy": int
    }
    RETURNS = ("count",)

class PartneredBigpharmas(Pharmacy.Query):
    ARGUMENTS = {
        "our_pharmacy": int
    }
    RETURNS = ("name", "phone")

class NotPartneredBigpharmas(Pharmacy.Query):
    ARGUMENTS = {
        "our_pharmacy": int
    }
    RETURNS = ("name", "phone")

class PotentialDrugs(Pharmacy.Query):
    ARGUMENTS = {
        "our_pharmacy": int
    }
    RETURNS = ("name",)

class DrugsFromOtherPharmas(Pharmacy.Query):
    ARGUMENTS = {
        "our_pharmacy": int
    }
    RETURNS = ("name",)


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

class DrugSearch(Pharmacy.Query):
    ARGUMENTS = {
        "our_pharmacy": int,
        "name": str,
        "formula": str,
        "min_price": int,
        "max_price": int,
        "drug": str
    }
    RETURNS = ("name", "formula", "bigpharma_id")

class PrescriptionSearch(Pharmacy.Query):
    ARGUMENTS = {
        "our_pharmacy": int,
        "patient": str,
        "doctor": str,
        "drug": str,
        "date": str
    }
    RETURNS = ("name", "doctor", "drug", "date", "dosage")
