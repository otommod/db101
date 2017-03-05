SCHEMA = {
    "patient": {
        "fields": ("id", "doctor_id", "name", "age", "address"),
        "key": "id",
    },
    "doctor": {
        "fields": ("id", "name", "specialty", "exp"),
        "key": "id",
    },
    "bigpharma": {
        "fields": ("id", "name", "phone"),
        "key": "id",
    },
    "pharmacy": {
        "fields": ("id", "name", "address", "phone"),
        "key": "id",
    },
    "drug": {
        "fields": ("id", "bigpharma_id", "name", "formula"),
        "key": "id",
    },
    "sell": {
        "fields": ("pharmacy_id", "drug_id", "price"),
        "key": ("pharmacy_id", "drug_id"),
    },
    "prescription": {
        "fields": ("patient_id", "doctor_id", "drug_id", "date", "dosage"),
        "key": ("patient_id", "doctor_id", "drug_id"),
    },
    "contract": {
        "fields": ("pharmacy_id", "bigpharma_id", "supervisor_id",
                   "start_date", "end_date", "content"),
        "key": ("pharmacy_id", "bigpharma_id"),
    },
}
