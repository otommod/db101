import wx


SELECT Drug.name,Sell.price,Drug.formula 
FROM Sell JOIN Drug
ON Sell.pharmacy_id=Drug.id;

SELECT Doctor.*,Patient.name
FROM Doctor LEFT JOIN Patient
ON Doctor.id=Patient.id;

SELECT Doctor.name,max(exp)
FROM Doctor
WHERE specialty = 'surgeon'
GROUP BY Doctor;
