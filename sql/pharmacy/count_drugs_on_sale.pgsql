SELECT COUNT(DISTINCT drug_id)
FROM Sell
WHERE Sell.pharmacy_id = %(our_pharmacy)s;
