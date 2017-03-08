-- The number of contracts for each BigPharma that end before the given date.

SELECT COUNT(id)
FROM Contract
WHERE pharmacy_id = %(our_pharmacy)s
GROUP BY bigpharma_id;
HAVING end_date < %s;
