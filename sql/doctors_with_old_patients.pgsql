CREATE VIEW DoctorsWithOldPatients AS
SELECT name
FROM Doctor
WHERE (SELECT AVG(age)
       FROM Patient
       WHERE Patient.doctor_id = Doctor.id) > 50;
