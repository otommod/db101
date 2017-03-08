from .sqlquery import SQLQuery, SQLSearchQuery


class CountDrugsOnSale(SQLQuery):
    QUERY_FILE = "pharmacy/count_drugs_on_sale"


class DrugsOnSale(SQLQuery):
    QUERY_FILE = "pharmacy/drugs_on_sale"


class PatientSearchMapper(SQLSearchQuery):
    QUERY_FILE = "patient_search"
    ESCAPE = {"name", "doctor", "address", "drug"}


class DoctorSearchMapper(SQLSearchQuery):
    QUERY_FILE = "doctor_search"
    ESCAPE = {"name", "specialty", "patient", "drug"}
