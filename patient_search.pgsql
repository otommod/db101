-Find Patient by Doctor, Name, Age, Address and any Drug he is taking (according to his prescriptions).
	SELECT name, age, address, Doctor.name FROM Patient, Doctor 
		WHERE Patient.doctor_id = Doctor.id 
		AND Patient.id=ANY(SELECT patient_id FROM Prescription 
			WHERE drug_id = ANY(SELECT drug_id from Sell 
				WHERE pharmacy_id=%(our_pharmacy)s)) 
		AND (CASE WHEN %(include_name)s THEN Patient.name LIKE '%%'||%(name)s||'%%' ESCAPE '=' ELSE true END) 
		AND (CASE WHEN %(include_maxage)s THEN age < %(maxage)s ELSE true END) 
		AND (CASE WHEN %(include_minage)s THEN age > %(minage)s ELSE true END) 
		AND (CASE WHEN %(include_doctor)s THEN doctor_id = ANY(SELECT id FROM Doctor 
			WHERE name LIKE '%%'||%(doctor)s||'%%' ESCAPE '=') ELSE true END) 
		AND (CASE WHEN %(include_address)s THEN address LIKE '%%'||%(address)s||'%%' ESCAPE '=' ELSE true END) 
		AND (CASE WHEN %(include_drug)s THEN id = ANY(SELECT patient_id FROM Prescription 
			WHERE drug_id = ANY(SELECT id FROM Drug 
				WHERE name LIKE '%%'||%(drug)s||'%%' ESCAPE '=')) ELSE true END);
