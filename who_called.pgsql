-Who Called Me?
	(CASE %s WHEN ANY(SELECT BigPharma.phone FROM BigPharma)
			THEN SELECT name, phone FROM BigPharma WHERE phone = %s
	         WHEN ANY(SELECT Pharmacy.phone FROM Pharmacy) 
		 	THEN SELECT name, phone FROM Pharmacy WHERE phone = %s
	         ELSE 'https://www.xo.gr/' END) 
	
