SELECT count(SELECT * FROM Drug 
		WHERE Drug.id = ANY(SELECT drug_id FROM Sell 
			WHERE Sell.pharmacy_id = (SELECT id FROM Pharmacy
				WHERE id = %(our_pharmacy)s)));

