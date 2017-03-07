-Find the BigPharmas that we work with.
	SELECT name, phone FROM BigPharma 
		WHERE BigPharma.id = ANY(SELECT bigpharma_id FROM Contract 
			WHERE start_date<CURRENT_DATE 
			AND end_date>CURRENT_DATE 
			AND Contract.pharmacy_id = %(our_pharmacy)s);
