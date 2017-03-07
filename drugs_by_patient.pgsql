-List all the drugs a Patient needs. 
	SELECT drug_id, date, dosage FROM Prescription 
		WHERE patient_id = (SELECT id FROM Patient 
			WHERE name = %s);
