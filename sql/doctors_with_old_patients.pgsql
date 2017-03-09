SELECT Doctor.name,
       ROUND(AVG(age), 0) AS avg_age
FROM Doctor
     JOIN Patient ON Patient.doctor_id = Doctor.id
GROUP BY Doctor.id
HAVING AVG(age) > 50;
