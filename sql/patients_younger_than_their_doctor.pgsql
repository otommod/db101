SELECT name
FROM Patient
WHERE age > (SELECT exp
             FROM Doctor
             WHERE Doctor.id = Patient.doctor_id)
;
