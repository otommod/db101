SELECT Drug.name,
       COUNT(pharmacy_id)
FROM Sells
     JOIN Drug ON Drug.id = Sells.drug_id
GROUP BY drug_id;
