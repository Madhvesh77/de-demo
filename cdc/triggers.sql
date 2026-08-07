CREATE OR REPLACE FUNCTION notify_new_payment()
RETURNS trigger
AS $$
BEGIN

    PERFORM pg_notify(
        'payments_channel',
        NEW.id::text
    );

    RETURN NEW;

END;
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS payment_trigger
ON payments;

CREATE TRIGGER payment_trigger
AFTER INSERT
ON payments
FOR EACH ROW
EXECUTE FUNCTION notify_new_payment();