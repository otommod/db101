from .model import Model


class General(Model):
    pass


class PatientCount(General.Query):
    # ARGUMENTS = {}
    RETURNS = ("count")


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


class CountContractsThatEndBefore(General.Query):
    ARGUMENTS = {
        "date": str
    }
    RETURNS = ("count",)


class CountContractsThatBeginAfter(General.Query):
    ARGUMENTS = {
        "date": str
    }
    RETURNS = ("count",)
