SELECT Drug.name,
       BigPharma.name AS maker,
       Drug.formula,
       Sell.price
FROM Drug
     JOIN BigPharma ON Drug.bigpharma_id = BigPharma.id
     JOIN Sell ON Drug.id = Sell.drug_id
WHERE Sell.pharmacy_id = %(our_pharmacy)s
;
