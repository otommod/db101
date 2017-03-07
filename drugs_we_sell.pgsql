SELECT name, formula, bigpharma_id FROM Drug 
		WHERE id = ANY(SELECT drug_id FROM Sell
			WHERE pharmacy_id = ANY(SELECT id FROM Pharmacy
				WHERE id = %(our_pharmacy)s)); 
