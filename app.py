import wx


STATEMENT = """
SELECT Drug.name, BigPharma.name AS maker, Drug.formula, Sell.price FROM
  Drug
  JOIN BigPharma ON Drug.bigpharma_id = BigPharma.id
  JOIN Sell ON Drug.id = Sell.drug_id
WHERE Sell.pharmacy_id = $1;
"""

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
    JOIN Sell ON Sell.drug_id = Prescription.drug_id AND Sell.pharmacy_id = $1;
"""
