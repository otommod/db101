-- The number of contracts for each BigPharma that end before the given date.

SELECT COUNT(id)
FROM Contract
GROUP BY bigpharma_id;
HAVING end_date < %s;
