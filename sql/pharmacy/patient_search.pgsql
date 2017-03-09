-- TODO: print Drug name
SELECT Patient.name,
       age,
       address,
       Doctor.name AS doctor
FROM Patient,
     Doctor
WHERE Patient.doctor_id = Doctor.id
  AND Patient.id = ANY(SELECT patient_id
                       FROM Prescription
                       WHERE drug_id = ANY(SELECT drug_id
                                           FROM Sell
                                           WHERE pharmacy_id = %(our_pharmacy)s))
  AND CASE
    WHEN %(include_name)s
    THEN Patient.name ILIKE '%%'||%(name)s||'%%' ESCAPE '='
    ELSE true
  END
  AND CASE
    WHEN %(include_age_max)s
    THEN age < %(age_max)s
    ELSE true
  END
  AND CASE
    WHEN %(include_age_min)s
    THEN age > %(age_min)s
    ELSE true
  END
  AND CASE
    WHEN %(include_doctor)s
    THEN doctor_id = ANY(SELECT id
                         FROM Doctor
                         WHERE name ILIKE '%%'||%(doctor)s||'%%' ESCAPE '=')
    ELSE true
  END
  AND CASE
    WHEN %(include_address)s
    THEN address ILIKE '%%'||%(address)s||'%%' ESCAPE '='
    ELSE true
  END
  AND CASE
    WHEN %(include_drug)s
    THEN Patient.id = ANY(SELECT patient_id
                  FROM Prescription
                WHERE drug_id = ANY(SELECT id
                                    FROM Drug
                                    WHERE name LIKE '%%'||%(drug)s||'%%' ESCAPE '='))
    ELSE true
  END
;
