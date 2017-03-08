-- The number of Contracts that start after the given date

SELECT COUNT(id)
FROM Contract
WHERE pharmacy_id = %(our_pharmacy)s
GROUP BY bigpharma_id;
HAVING start_date < %s;
