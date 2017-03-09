SELECT name,
       specialty,
       exp
FROM Doctor
WHERE id = ANY(SELECT doctor_id
               FROM Prescription
               WHERE drug_id = ANY(SELECT drug_id
                                   FROM Sell
                                   WHERE pharmacy_id = %(our_pharmacy)s))
  AND CASE
    WHEN %(include_name)s
    THEN Doctor.name ILIKE '%%'||%(name)s||'%%' ESCAPE '='
    ELSE true
  END
  AND CASE
    WHEN %(include_specialty)s
    THEN specialty ILIKE '%%'||%(specialty)s||'%%' ESCAPE '='
    ELSE true
  END
  AND CASE
    WHEN %(include_exp)s
    THEN exp = %(exp)s
    ELSE true
  END
  AND CASE
    WHEN %(include_patient)s
    THEN Doctor.id = ANY(SELECT doctor_id
                         FROM Patient
                         WHERE name ILIKE '%%'||%(patient)s||'%%' ESCAPE '=')
    ELSE true
  END
  AND CASE
    WHEN %(include_drug)s
    THEN Doctor.id = ANY(SELECT doctor_id
                         FROM Prescription
                         WHERE drug_id = ANY(SELECT id
                                             FROM Drug
                                             WHERE name ILIKE '%%'||%(drug)s||'%%' ESCAPE '='))
    ELSE true
  END
;
