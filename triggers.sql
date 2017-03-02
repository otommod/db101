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
