SELECT COUNT(*)
FROM Contract
WHERE pharmacy_id = %(our_pharmacy)s
  AND CASE %(date_type)s
    WHEN 'end'   THEN end_date < %(date)s
    WHEN 'start' THEN start_date < %(date)s
  END
;
