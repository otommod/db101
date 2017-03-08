SELECT Drug.name,
       date,
       dosage
FROM Prescription
     JOIN Drug ON Drug.id = Prescription.drug_id
WHERE patient_id = (SELECT id FROM Patient WHERE name = %s);
