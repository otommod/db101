from .model import Model


class General(Model):
    pass


class PatientCount(General.Query):
    RETURNS = ("count")
