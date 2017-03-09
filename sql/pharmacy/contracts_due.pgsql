SELECT *
FROM Contract
WHERE pharmacy_id = %(our_pharmacy)s
ORDER BY end_date;
