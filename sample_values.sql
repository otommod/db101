INSERT INTO Doctor(name, specialty, exp) VALUES
    ('Dr.George', 'general', 5),
    ('Dr.Babis', 'surgeon', 15),
    ('Dr.Maria', 'surgeon', 27),
    ('Dr.Otto', 'general', 8);
    
INSERT INTO Patient(doctor_id, name, age, address) VALUES
    (1, 'Miltos', 22, 'Athens'),
    (1, 'Maria', 21, 'London'),
    (2, 'Robert', 25, 'Seattle'),
    (2, 'Margaret', 23, 'Redmond');

INSERT INTO BigPharma(name, phone) VALUES
    ('AtticaDrugs', '210-6359632');

INSERT INTO Pharmacy(name, address, phone) VALUES
    ('Pharmacy1', 'Agias Elenis 8, Athens', '210-8977502'),
    ('Pharmacy2', 'Synopis 7, Athens', '210-9063341');

INSERT INTO Drug(bigpharma_id, name, formula) VALUES
    (1, 'Laferol', 'CaONBa'),
    (1, 'Nitropol', 'NC2');

INSERT INTO Sell(pharmacy_id, drug_id, price) VALUES
    (1, 1, 105),
    (2, 2, 33);

INSERT INTO Prescription(patient_id, doctor_id, drug_id, date, dosage) VALUES
    (2, 1, 1, '2016-05-14', 2),
    (3, 2, 1, '2016-05-20', 3);

INSERT INTO Contract(pharmacy_id, bigpharma_id, supervisor_id, start_date, end_date, content) VALUES
    (1, 1, 1, '2015-12-08', '2017-12-08', 'This contract ...');
