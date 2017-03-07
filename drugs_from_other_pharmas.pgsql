-List all drugs made by Pharmas that are NOT currently under contract with us.
	SELECT name FROM Drug 
		WHERE bigpharma_id <> ALL(SELECT id FROM BigPharma 
			WHERE id = ANY(SELECT bigpharma_id FROM Contract
				WHERE start_date<CURRENT_DATE
				AND end_date>CURRENT_DATE 
				AND pharmacy_id=%(our_pharmacy)s));
