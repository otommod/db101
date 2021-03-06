-- http://www.isathens.gr/giatroi/members-search-engine.html
INSERT INTO Doctor(name, specialty, exp) VALUES
    ('Νάνος Ευάγγελος',         'surgeon',          38),
    ('Μέγας Γεώργιος',          'urologist',        15),
    ('Μπαιρακτάρης Ανδρέας',    'neurosurgeon',     38),
    ('Ματθαίος Μαρίνος',        'cardiologist',     26),
    ('Νικολόπουλος Γεώργιος',   'gynecologist',     19),
    ('Ταραντίνος Ροδόλφος',     'pulmonologist',    28),
    ('Παντελής Δημήτριος',      'ophthalmologist',  31),
    ('Φελέκης Δημήτριος',       'otolaryngologist', 16),
    ('Φέττα Μελπομένη',         'otolaryngologist', 25);

-- https://getfakedata.com/person/el_GR
INSERT INTO Patient(doctor_id, name, age, address) VALUES
    (1, 'Δήμος Ταμτάκος',       56, 'Σαλαμίνος 43, Ασπρόπυργος'),
    (2, 'Λάσκαρης Αθανασιάδης', 24, 'Αετοράχης 40, Γαλάτσι'),
    (2, 'Σωτήριος Ιατρίδης',    40, 'Αλκηβιάδου 81, Πειραιάς'),
    (3, 'Ευριπίδης Ρούσσος',    18, 'Θράκης 11, Χαϊδάρι'),
    (4, 'Λαυρέντιος Πολίτης',   38, 'Μιλτιάδου 17, Αθήνα'),
    (4, 'Άνθιμος Παπαγεωργίου', 47, 'Λάμπρου Κατσώνη 97, Μοσχάτο'),
    (5, 'Χρυσαυγή Μακρή',       43, 'Δελφών 37, Ηράκλειο'),
    (6, 'Ξενοφών Παπαδόπουλος', 22, 'Πλατεών 49, Μαρούσι'),
    (7, 'Κλειώ Γιαννακοπούλου', 33, 'Αρχιμήδους 14, Αιγάλεω'),
    (7, 'Χάρη Γερμανού',        34, 'Κεφαλληνίας 4, Άγιος Δημήτριος'),
    (8, 'Ασήμης Κυριακόπουλος', 19, 'Μενάνδρου 17, Χαλάνδρι'),
    (9, 'Κυριαζής Αλαφούζος',   39, 'Κερκύρας 19, Γλυκά Νερά');

INSERT INTO BigPharma(name, phone) VALUES
    ('Adelco',            '210-4819311'),
    ('Qualia Pharma',     '210-6256177'),
    ('Pharmathen',        '210-6604300'),
    ('Νόρμα Ελλάς α.ε.',  '210-5222282'),
    ('Remedina Α.Β.Ε.Ε.', '210-2385552'),
    ('Galenica',          '210-5220922');

INSERT INTO Drug(bigpharma_id, name, formula) VALUES
    (1, 'Adeprenal',  'C20-H21-F-N2-O'),
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
    ('Pharmacylive',        'Λουίζης Ριανκούρ 57, Αθήνα',       '211-0131194'),
    ('Ακρόπολις Φαρμακείο', 'Διονυσίου Αεροπαγίτου 10, Αθήνα',  '215-2151610'),
    ('One Click Pharmacy',  'Φιλαδέλφειας 26, Αιγάλεω',         '210-5912888'),
    ('Our Pharmacy',        'Πανόρμου 34, Αθήνα',               '210-6914630'),
    ('Dr Pharmacy Marousi', 'Λεωφόρος Κηφισίας 78, Μαρούσι',    '211-4114140');

INSERT INTO Contract(pharmacy_id, bigpharma_id, start_date, end_date, content) VALUES
    (1, 1, '2015-12-08', '2018-12-08', 'This contract...'),
    (1, 2, '2016-02-01', '2017-08-01', 'This other contract...'),
    (1, 3, '2015-05-30', '2019-01-01', 'You get the point...'),
    (1, 5, '2014-09-03', '2017-09-03', '...'),
    (2, 1, '2016-10-18', '2018-10-18', '...'),
    (2, 2, '2014-03-24', '2017-03-24', '...'),
    (2, 4, '2014-09-11', '2018-01-01', '...'),
    (3, 1, '2015-04-30', '2017-11-11', '...'),
    (3, 2, '2016-01-09', '2017-07-25', '...'),
    (3, 3, '2012-10-16', '2017-03-16', '...'),
    (3, 4, '2017-01-20', '2019-10-01', '...'),
    (4, 1, '2014-02-27', '2018-04-02', '...'),
    (4, 2, '2015-12-03', '2019-12-03', '...'),
    (4, 3, '2015-09-23', '2017-09-23', '...'),
    (4, 4, '2013-11-05', '2018-01-01', '...'),
    (4, 5, '2014-07-24', '2019-10-03', '...'),
    (4, 6, '2013-08-01', '2017-08-01', '...'),
    (5, 1, '2015-10-10', '2019-04-10', '...'),
    (5, 2, '2016-02-13', '2020-02-13', '...'),
    (5, 4, '2013-05-24', '2018-11-01', '...'),
    (5, 5, '2013-05-18', '2017-09-21', '...'),
    (5, 6, '2015-09-03', '2019-09-03', '...');

INSERT INTO Sell(pharmacy_id, drug_id, price) VALUES
-- 1st pharmacy
    (1, 1, 105),
    (1, 3, 62),
    (1, 4, 77),
    (1, 8, 43),
    (1, 14, 24),
-- 2nd pharmacy
    (2, 1, 90),
    (2, 2, 44),
    (2, 4, 80),
    (2, 10, 41),
    (2, 11, 124),
    (2, 12, 12),
-- 3rd pharmacy
    (3, 1, 111),
    (3, 2, 50),
    (3, 5, 33),
    (3, 6, 85),
    (3, 7, 60),
    (3, 8, 32),
    (3, 9, 94),
    (3, 10, 40),
-- 4th pharmacy
    (4, 3, 62),
    (4, 6, 83),
    (4, 8, 39),
    (4, 11, 122),
    (4, 13, 201),
    (4, 14, 19),
    (4, 17, 52),
-- 5th pharmacy
    (5, 2, 47),
    (5, 5, 35),
    (5, 12, 10),
    (5, 14, 21),
    (5, 15, 214),
    (5, 16, 82);

INSERT INTO Prescription(patient_id, doctor_id, drug_id, date, dosage) VALUES
    (2,  2, 1,  '2017-04-14', 2),
    (3,  2, 5,  '2017-05-20', 3),
    (1,  1, 8,  '2017-07-07', 1),
    (9,  7, 12, '2017-06-10', 1),
    (4,  3, 4,  '2017-08-22', 2),
    (10, 7, 16, '2017-06-15', 2),
    (7,  5, 10, '2017-07-01', 3),
    (11, 8, 7,  '2017-04-12', 2),
    (5,  4, 3,  '2017-03-10', 3),
    (8,  6, 2,  '2017-04-27', 1),
    (6,  4, 11, '2017-06-05', 2),
    (12, 9, 4,  '2017-08-13', 1);
