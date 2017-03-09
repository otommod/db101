SELECT Drug.name,
       COUNT(pharmacy_id)
FROM Sell
     JOIN Drug ON Drug.id = Sell.drug_id
GROUP BY Drug.name;
