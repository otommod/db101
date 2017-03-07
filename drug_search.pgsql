-Find Drug by Pharma, Formula, PriceRange and whether we are selling it.
	SELECT name, formula, bigpharma_id FROM Drug 
		WHERE (CASE WHEN %(include_price)s THEN (SELECT price FROM Sell 
				WHERE Sell.drug_id = Drug.id) > %(min_price)s 
			AND    (SELECT price FROM Sell 
				WHERE Sell.drug_id = Drug.id) < %(max_price)s ELSE true END) 
		AND (CASE WHEN %(include_name)s THEN name LIKE '%%'||%(name)s||'%%' ESCAPE '=' ELSE true END) 
		AND (CASE WHEN %(include_formula)s THEN formula LIKE '%%'||%(formula)s||'%%' ESCAPE '=' ELSE true END) 
		AND (CASE WHEN %(we_sell)s THEN Drug.id = ANY(SELECT drug_id FROM Sell
			WHERE pharmacy_id = ANY(SELECT id FROM Pharmacy 
				WHERE Pharmacy.id=%(our_pharmacy)s)) ELSE true END)
		AND (CASE WHEN %(we_dont_sell)s THEN Drug.id <> ALL(SELECT drug_id FROM Sell
			WHERE pharmacy_id = ANY(SELECT id FROM Pharmacy 
				WHERE Pharmacy.id=%(our_pharmacy)s)) ELSE true END);
