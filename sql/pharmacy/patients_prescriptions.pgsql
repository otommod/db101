SELECT Patient.name AS patient,
       Doctor.name AS doctor,
       Drug.name AS drug,
       date,
       dosage
FROM Prescription
     JOIN Patient ON Patient.id = Prescription.patient_id
     JOIN Doctor ON Doctor.id = Prescription.doctor_id
     JOIN Drug ON Drug.id = Prescription.drug_id
     JOIN Sell ON Sell.drug_id = Prescription.drug_id
              AND Sell.pharmacy_id = %(our_pharmacy)s
;
