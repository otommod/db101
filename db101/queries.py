STATEMENT = """
SELECT Drug.name, BigPharma.name AS maker, Drug.formula, Sell.price FROM
  Drug
  JOIN BigPharma ON Drug.bigpharma_id = BigPharma.id
  JOIN Sell ON Drug.id = Sell.drug_id
WHERE Sell.pharmacy_id = %s;
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
    WHERE (SELECT AVG(age) FROM Patient WHERE Patient.doctor_id = Doctor.id) > 50;
"""
