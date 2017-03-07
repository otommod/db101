-- TODO: relation is not total
CREATE TABLE Doctor (
  id SERIAL PRIMARY KEY,
  name TEXT,
  specialty TEXT,
  exp INTEGER
);

CREATE TABLE Patient (
  id SERIAL PRIMARY KEY,
  doctor_id INTEGER REFERENCES Doctor(id),
  name TEXT,
  age INTEGER,
  address TEXT
);

CREATE TABLE BigPharma (
  id SERIAL PRIMARY KEY,
  name TEXT,
  phone TEXT
);

CREATE TABLE Pharmacy (
  id SERIAL PRIMARY KEY,
  name TEXT,
  address TEXT,
  phone TEXT
);

CREATE TABLE Drug (
  id SERIAL PRIMARY KEY,
  bigpharma_id INTEGER REFERENCES BigPharma(id),
  name TEXT,
  formula TEXT
);

-- TODO: relation is not total
CREATE TABLE Sell (
  pharmacy_id INTEGER REFERENCES Pharmacy(id),
  drug_id INTEGER REFERENCES Drug(id),
  price INTEGER,
  CONSTRAINT sell_key PRIMARY KEY(pharmacy_id, drug_id)
);

CREATE TABLE Prescription (
  patient_id INTEGER REFERENCES Patient(id),
  doctor_id INTEGER REFERENCES Doctor(id),
  drug_id INTEGER REFERENCES Drug(id),
  date DATE,
  dosage INTEGER,
  CONSTRAINT prescription_key PRIMARY KEY (patient_id, doctor_id, drug_id)
);

-- TODO: relation is not total
CREATE TABLE Contract (
  pharmacy_id INTEGER REFERENCES Pharmacy(id),
  bigpharma_id INTEGER REFERENCES BigPharma(id),
  supervisor ΤΕΧΤ,
  start_date DATE,
  end_date DATE,
  content TEXT,
  CONSTRAINT contract_key PRIMARY KEY (pharmacy_id, bigpharma_id)
);


CREATE OR REPLACE FUNCTION has_contract_for_drug(integer, integer) RETURNS bool AS $$
    SELECT EXISTS(
        SELECT * FROM
            Contract
            JOIN Drug ON Contract.bigpharma_id = Drug.bigpharma_id
        WHERE Contract.pharmacy_id = $1 AND Drug.id = $2);
$$ LANGUAGE 'SQL';

ALTER TABLE Sell ADD CONSTRAINT has_contract CHECK (has_contract_for_drug(pharmacy_id, drug_id));
