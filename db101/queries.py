STATEMENT2 = """
SELECT Doctor.*, Patient.name FROM
  Doctor
  LEFT JOIN Patient ON Doctor.id = Patient.doctor_id;
"""

STATEMENT3 = """
SELECT Patient.name AS patient,
       Doctor.name AS doctor,
       Drug.name AS drug,
       date,
       dosage
FROM
  Prescription
  JOIN Patient ON Patient.id = Prescription.patient_id
  JOIN Doctor ON Doctor.id = Prescription.doctor_id
  JOIN Drug ON Drug.id = Prescription.drug_id
  JOIN Sell ON Sell.drug_id = Prescription.drug_id AND Sell.pharmacy_id = %s;
"""

AGGREGATE = """
SELECT COUNT(id) FROM Patient;
"""

GROUP_BY = """
SELECT COUNT(pharmacy_id)
FROM Sells
GROUP BY drug_id;
"""

ORDER_BY = """
SELECT *
FROM Contract
ORDER BY end_date;
"""

GROUP_BY_HAVING = """
SELECT COUNT(id)
FROM Contract
GROUP BY bigpharma_id;
HAVING end_date < %s;
"""

NESTED = """
SELECT name FROM Patient
    WHERE age > (SELECT exp FROM Doctor WHERE Doctor.id = Patient.doctor_id);
"""

NESTED2 = """
SELECT name FROM Doctor
WHERE (SELECT AVG(age)
       FROM Patient
       WHERE Patient.doctor_id = Doctor.id) > 50
;
"""


class QueryMetaclass(type):
    def __init__(cls, name, bases, attrs):
        if not hasattr(cls, "ALL"):
            cls.ALL = {}
        if hasattr(cls, "RETURNS"):
            cls.ALL[name] = cls

        super().__init__(name, bases, attrs)


class Query(metaclass=QueryMetaclass):
    @classmethod
    def validate(cls, named_params):
        for p, v in named_params.items():
            if p not in cls.ARGUMENTS:
                return False
            try:
                cls.ARGUMENTS[p](v)
                return True
            except ValueError:
                return False


class DrugsOnSale(Query):
    ARGUMENTS = {
        "our_pharmacy": int
    }
    RETURNS = ("name", "maker", "formula", "price")


class CountDrugsOnSale(Query):
    ARGUMENTS = {
        "our_pharmacy": int
    }
    RETURNS = ("count")


class SearchQuery(Query):
    pass


class PatientSearchMapper(SearchQuery):
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


class DoctorSearchMapper(SearchQuery):
    ARGUMENTS = {
        "our_pharmacy": int,
        "name": str,
        "specialty": str,
        "exp": int,
        "patient": str,
        "drug": str
    }
    RETURNS = ("name", "specialty", "exp")
