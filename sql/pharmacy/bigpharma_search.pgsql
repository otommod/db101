SELECT name,
       phone
FROM BigPharma
WHERE CASE
    WHEN %(include_name)s
    THEN BigPharma.name ILIKE '%%'||%(name)s||'%%' ESCAPE '='
    ELSE true
  END
  AND CASE
    WHEN %(include_phone)s
    THEN BigPharma.phone ILIKE '%%'||%(phone)s||'%%' ESCAPE '='
    ELSE true
  END
  AND CASE
    WHEN %(include_drug)s
    THEN BigPharma.id = ANY(SELECT bigpharma_id
                            FROM Drug
                            WHERE name ILIKE '%%'||%(drug)s||'%%' ESCAPE '=')
    ELSE true
  END
  AND CASE
    WHEN %(include_contract)s
    THEN BigPharma.id = ANY(SELECT bigpharma_id
                            FROM Contract
                            WHERE start_date > %(start_date)s
                              AND end_date < %(end_date)s)
    ELSE true
  END
;
