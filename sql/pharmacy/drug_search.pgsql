SELECT name,
       formula,
       bigpharma_id
FROM Drug
WHERE CASE
    WHEN %(include_price)s
    THEN (SELECT price
          FROM Sell
          WHERE Sell.drug_id = Drug.id) > %(price_min)s
     AND (SELECT price
          FROM Sell
          WHERE Sell.drug_id = Drug.id) < %(price_max)s
    ELSE true
  END
  AND CASE
    WHEN %(include_name)s
    THEN name ILIKE '%%'||%(name)s||'%%' ESCAPE '='
    ELSE true
  END
  AND CASE
    WHEN %(include_formula)s
    THEN formula ILIKE '%%'||%(formula)s||'%%' ESCAPE '='
    ELSE true
  END
  AND CASE
    WHEN %(we_sell)s
    THEN Drug.id = ANY(SELECT drug_id
                        FROM Sell
			WHERE pharmacy_id = ANY(SELECT id
                                                FROM Pharmacy
                                                WHERE Pharmacy.id = %(our_pharmacy)s))
    ELSE true
  END
  AND CASE
    WHEN %(we_dont_sell)s
    THEN Drug.id <> ALL(SELECT drug_id
                        FROM Sell
			WHERE pharmacy_id = ANY(SELECT id
                                                FROM Pharmacy 
                                                WHERE Pharmacy.id = %(our_pharmacy)s))
    ELSE true
  END
;
