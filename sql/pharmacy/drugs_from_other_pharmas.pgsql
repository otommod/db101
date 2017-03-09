SELECT Drug.name AS drug,
       BigPharma.name AS maker
FROM Drug
     JOIN BigPharma ON BigPharma.id = Drug.bigpharma_id
WHERE bigpharma_id <> ALL(SELECT id
                          FROM BigPharma
                          WHERE id = ANY(SELECT bigpharma_id
                                         FROM ActiveContracts
                                         WHERE pharmacy_id = %(our_pharmacy)s))
;
