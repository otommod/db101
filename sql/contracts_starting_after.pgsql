-- The number of Contracts that start after the given date

SELECT COUNT(id)
FROM Contract
GROUP BY bigpharma_id;
HAVING start_date < %s;
