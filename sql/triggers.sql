CREATE OR REPLACE FUNCTION before_remove_bigpharma() RETURNS trigger AS $$
    BEGIN
        DELETE FROM Sell WHERE drug_id = ANY(SELECT id FROM Drug WHERE bigpharma_id = OLD.id);
        DELETE FROM Prescription WHERE drug_id = ANY(SELECT id FROM Drug WHERE bigpharma_id = OLD.id);
        DELETE FROM Contract WHERE bigpharma_id = OLD.id;
        DELETE FROM Drug WHERE bigpharma_id = OLD.id;
        RETURN OLD;
    END;
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS before_remove_bigpharma ON BigPharma;
CREATE TRIGGER before_remove_bigpharma
    BEFORE DELETE ON BigPharma
    FOR EACH ROW EXECUTE PROCEDURE before_remove_bigpharma();


CREATE OR REPLACE FUNCTION before_remove_contract() RETURNS trigger AS $$
    BEGIN
        DELETE FROM Sell
            WHERE pharmacy_id = OLD.pharmacy_id AND drug_id = ANY(
                SELECT id FROM Drug WHERE bigpharma_id = OLD.bigpharma_id
            );
        RETURN OLD;
    END;
$$ LANGUAGE 'plpgsql';

DROP TRIGGER IF EXISTS before_remove_contract ON Contract;
CREATE TRIGGER before_remove_contract
    BEFORE DELETE ON Contract
    FOR EACH ROW EXECUTE PROCEDURE before_remove_contract();
