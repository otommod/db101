
SELECT name, formula 
FROM Drug
	WHERE (SELECT avg(age) FROM Patient
	WHERE Patient.id = ANY(SELECT patient_id FROM Prescription
		WHERE Prescription.drug_id = ANY(SELECT id FROM Drug))) > 50;
