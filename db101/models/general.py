from .model import Model


class General(Model):
    pass


class PatientCount(General.Query):
    # ARGUMENTS = {}
    RETURNS = ("count")


class CountPatients(General.Query):
    ARGUMENTS = {}
    RETURNS = ("count",)

class CountPharmaciesByDrug(General.Query):
    ARGUMENTS = {}
    RETURNS = ("name", "count")

class PatientsAndDoctors(General.Query):
    ARGUMENTS = {}
    RETURNS = ("name", "doctor", "specialty")

class BigpharmaSearch(General.Query):
    ARGUMENTS = {
        "name": str,
        "phone": str,
        "start_date": str,
        "end_date": str,
        "drug": str,
    }
    RETURNS = ("name", "phone")


class WhoCalled2(General.Query):
    ARGUMENTS = {
        "phone": str
    }
    RETURNS = ("name", "phone")


class DrugsForPatient(General.Query):
    ARGUMENTS = {
        "name": str,
    }
    RETURNS = ("drug_id", "date", "dosage")


class DoctorsWithOldPatients(General.Query):
    # ARGUMENTS = {}
    RETURNS = ("name",)
