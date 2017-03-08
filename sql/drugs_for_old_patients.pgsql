-- The drugs that old (older than 50 years old) patients use.

SELECT Drug.name,
       Drug.formula
FROM Drug
WHERE (SELECT AVG(age)
       FROM Patient
       WHERE Patient.id = ANY(SELECT patient_id
                              FROM Prescription
                              WHERE Prescription.drug_id = ANY(SELECT id FROM Drug))) > 50;

