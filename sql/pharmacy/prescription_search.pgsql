SELECT Patient.name,
       Doctor.name AS doctor,
       Drug.name AS drug,
       date,
       dosage
FROM Patient,
     Doctor,
     Drug,
     (SELECT patient_id,
             doctor_id,
             drug_id,
             date,
             dosage
      FROM Prescription
      WHERE CASE
          WHEN %(include_doctor)s
          THEN doctor_id = ANY(SELECT id
                               FROM Doctor
                               WHERE name LIKE '%%'||%(doctor)s||'%%' ESCAPE '=')
          ELSE true
        END
        AND CASE
          WHEN %(include_patient)s
          THEN patient_id = ANY(SELECT id
                                FROM Patient
				WHERE name LIKE '%%'||%(patient)s||'%%' ESCAPE '=')
          ELSE true
        END
	AND CASE
          WHEN %(include_date)s
          THEN date = %(date)s
          ELSE true
        END
        AND CASE
          WHEN %(include_drug)s
          THEN drug_id = ANY(SELECT id
                             FROM Drug
                             WHERE name LIKE '%%'||%(drug)s||'%%' ESCAPE '=')
          ELSE true END)
     ) AS prescription_shit
WHERE prescription_shit.patient_id = Patient.id
  AND prescription_shit.doctor_id = Doctor.id
  AND prescription_shit.drug_id = Drug.id 
  AND Drug.id = ANY(SELECT drug_id
                    FROM Sell
                    WHERE pharmacy_id = %(our_pharmacy)s)
;
