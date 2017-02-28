-- http://www.isathens.gr/giatroi/members-search-engine.html
INSERT INTO Doctor(name, specialty, exp) VALUES
    ('Ρίζος Σπυρίδων',          'surgeon',          33),
    ('Νάνος Ευάγγελος',         'surgeon',          38),
    ('Μέγας Γεώργιος',          'urologist',        15),
    ('Σπυριδάκη Σωτηρία',       'neurologist',      27),
    ('Μπαιρακτάρης Ανδρέας',    'neurosurgeon',     38),
    ('Ματθαίος Μαρίνος',        'cardiologist',     26),
    ('Νικολόπουλος Γεώργιος',   'gynecologist',     19),
    ('Ταραντίνος Ροδόλφος',     'pulmonologist',    28),
    ('Μπαξεβανάκης Αναστάσιος', 'ophthalmologist',  24),
    ('Παντελής Δημήτριος',      'ophthalmologist',  31),
    ('Φελέκης Δημήτριος',       'otolaryngologist', 16),
    ('Φέττα Μελπομένη',         'otolaryngologist', 25);

INSERT INTO Patient(doctor_id, name, age, address) VALUES
    (1, 'Miltos', 22, 'Athens'),
    (1, 'Maria', 21, 'London'),
    (2, 'Robert', 25, 'Seattle'),
    (2, 'Margaret', 23, 'Redmond');

INSERT INTO BigPharma(name, phone) VALUES
    ('Adelco', '210-4819311'),
    ('Qualia Pharma', '210-6256177'),
    ('Pharmathen', '210-6604300'),
    ('Νόρμα Ελλάς α.ε.', '210-5222282'),
    ('Remedina Α.Β.Ε.Ε.', '210-2385552'),
    ('Galenica', ' 210-5220922');

INSERT INTO Drug(bigpharma_id, name, formula) VALUES
    (1, 'Adeprenal',  'C20-H21-F-N2O'),
    (1, 'Saturnil',   'C17-H13-Cl-N4'),
    (1, 'Filicine',   'C19-H19-N7-O6'),
    (2, 'Zalasta',    'C17-H20-N4-S'),
    (2, 'Certorun',   'C17-H17-Cl2-N'),
    (2, 'Vizarsin',   'C22-H30-N6-O4-S'),
    (3, 'Labilex',    'C18-H18-N8-O7-S3'),
    (3, 'Nelabocin',  'C16-H16-N4-O8-S'),
    (4, 'Bindazac',   'C13-H22-N4-O3-S'),
    (4, 'Letynol',    'C16-H17-N5-O7-S2'),
    (4, 'Staphyclox', 'C19-H18-Cl-N3-O5-S'),
    (4, 'Trinalin',   'C7-H15-N-O3'),
    (4, 'Chloranic',  'C11-H12-Cl2-N2-O5'),
    (5, 'Merovia',    'C17-H25-N3-O5-S'),
    (6, 'Biofenac',   'C16-H13-Cl2-N-O4'),
    (6, 'Remodulin',  'C23-H34-O5'),
    (6, 'Photofrin',  'C68-H74-N8-O11');

INSERT INTO Pharmacy(name, address, phone) VALUES
    ('Pharmacy1', 'Agias Elenis 8, Athens', '210-8977502'),
    ('Pharmacy2', 'Synopis 7, Athens', '210-9063341');

INSERT INTO Sell(pharmacy_id, drug_id, price) VALUES
    (1, 1, 105),
    (2, 2, 33);

INSERT INTO Prescription(patient_id, doctor_id, drug_id, date, dosage) VALUES
    (2, 1, 1, '2016-05-14', 2),
    (3, 2, 1, '2016-05-20', 3);

INSERT INTO Contract(pharmacy_id, bigpharma_id, supervisor_id, start_date, end_date, content) VALUES
    (1, 1, 1, '2015-12-08', '2017-12-08', 'This contract ...');
