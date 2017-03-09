SELECT Patient.name,
       Doctor.name AS doctor,
       Doctor.specialty
FROM Doctor
     LEFT JOIN Patient ON Doctor.id = Patient.doctor_id;
