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
        "fields": ("pharmacy_id", "bigpharma_id", "supervisor",
                   "start_date", "end_date", "content"),
        "key": ("pharmacy_id", "bigpharma_id"),
    },
    "activecontracts": {
        "fields": ("pharmacy_id", "bigpharma_id", "supervisor",
                   "start_date", "end_date", "content"),
        "key": ("pharmacy_id", "bigpharma_id"),
    },
    "phones": {
        "fields": ("name", "phone"),
        "key": ("name", "phone"),
    }
}

QUERIES = {
    "general": {
        "sql/count_patients.pgsql": {
            "arguments": (),
            "returns": ("count",)
        },
        "sql/count_pharmacies_by_drug.pgsql": {
            "arguments": (),
            "returns": ("name", "count"),
        },
        "sql/doctors_with_old_patients.pgsql": {
            "arguments": (),
            "returns": ("name", "avg_age")
        },
        "sql/drugs_for_old_patients.pgsql": {
            "arguments": (),
            "returns": ("name", "formula"),
        },
        "sql/patients_and_doctors.pgsql": {
            "arguments": (),
            "returns": ("name", "doctor", "specialty"),
        },
        "sql/drugs_of_patient.pgsql": {
            "arguments": ("name",),
            "returns": ("drug", "date", "dosage")
        },

        # "sql/patients_younger_than_their_doctor.pgsql",
        # "people.pgsql",
        # "who_called.pgsql",
        # "who_called_2.pgsql",
    },

    "pharmacy": {
        "sql/pharmacy/count_contracts_by_date.pgsql": {
            "arguments": ("date",),
            "returns": ("count",)
        },
        "sql/pharmacy/contracts_due.pgsql": {
            "arguments": (),
            "returns": ("pharmacy_id", "bigpharma_id", "supervisor_id",
                        "start_date", "end_date", "content")
        },
        "sql/pharmacy/drugs_on_sale.pgsql": {
            "arguments": (),
            "returns": ("name", "maker", "formula", "price")
        },
        "sql/pharmacy/count_drugs_on_sale.pgsql": {
            "arguments": (),
            "returns": ("count",)
        },
        "sql/pharmacy/partnered_bigpharmas.pgsql": {
            "arguments": (),
            "returns": ("name", "phone"),
        },
        "sql/pharmacy/not_partnered_bigpharmas.pgsql": {
            "arguments": (),
            "returns": ("name", "phone")
        },
        "sql/pharmacy/potential_drugs.pgsql": {
            "arguments": (),
            "returns": ("name",)
        },
        "sql/pharmacy/drugs_from_other_pharmas.pgsql": {
            "arguments": (),
            "returns": ("drug", "maker")
        },
        "sql/pharmacy/patient_search.pgsql": {
            "__type__": "search",
            "arguments": ("our_pharmacy", "name", "age_min", "age_max",
                          "doctor", "address", "drug"),
            "returns": ("name", "age", "address", "doctor")
        },
        "sql/pharmacy/doctor_search.pgsql": {
            "__type__": "search",
            "arguments": ("our_pharmacy", "name", "specialty", "exp",
                          "patient", "drug"),
            "returns": ("name", "specialty", "exp")
        },
        "sql/pharmacy/drug_search.pgsql": {
            "__type__": "search",
            "arguments": ("name", "formula", "price_min", "price_max",
                          "drug"),
            "returns": ("name", "formula", "bigpharma_id")
        },
        "sql/pharmacy/prescription_search.pgsql": {
            "__type__": "search",
            "arguments": ("our_pharmacy", "patient", "doctor", "drug", "date"),
            "returns": ("name", "doctor", "drug", "date", "dosage")
        },
        "sql/pharmacy/patients_prescriptions.pgsql": {
            "arguments": (),
            "returns": ("patient", "doctor", "drug", "date", "dosage")
        }
    }
}
