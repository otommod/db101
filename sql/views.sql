CREATE VIEW doctors AS
    SELECT name, 'doctor', specialty
    FROM Doctor;

CREATE VIEW patients AS
    SELECT Patient.name, 'patient', Drug.name
    FROM Patient, Drug
    WHERE Drug.id = ANY(SELECT Prescription.drug_id FROM Prescription WHERE Prescription.patient_id = Patient.id);

CREATE VIEW people AS (doctors UNION patients) ORDER BY name;

CREATE VIEW phones AS
  SELECT name, phone FROM BigPharma
UNION
  SELECT name, phone FROM Pharmacy
;

CREATE VIEW ActiveContracts AS
SELECT *
FROM Contract
WHERE start_date < CURRENT_DATE
  AND end_date > CURRENT_DATE
;
