SELECT name
FROM Drug
WHERE id <> ALL(SELECT drug_id
                FROM Sell
                WHERE pharmacy_id=%(our_pharmacy)s)
  AND Drug.bigpharma_id = ANY(SELECT id
                              FROM BigPharma
                              WHERE id = ANY(SELECT bigpharma_id
                                             FROM Contract
                                             WHERE start_date < CURRENT_DATE 
                                               AND end_date > CURRENT_DATE))
;
