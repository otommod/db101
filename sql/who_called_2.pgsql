SELECT name,
       phone
FROM (CASE %s
    WHEN ANY(SELECT BigPharma.phone FROM BigPharma) THEN BigPharma
    WHEN ANY(SELECT Pharmacy.phone FROM Pharmacy) THEN Pharmacy
  END)
WHERE phone = %s
