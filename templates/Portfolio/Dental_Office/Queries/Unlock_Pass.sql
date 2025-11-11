CREATE OR REPLACE FUNCTION Unlock_Loyalty_Pass()
RETURNS VOID AS $$
BEGIN
    UPDATE billing
    SET amount_required = amount_required * 0.9
    WHERE appointment_num IN (
        SELECT a.appointment_num
        FROM appointments a
        JOIN patients p ON a.patient_id = p.patient_id
        WHERE p.loyalty_pass = TRUE
    );
END;
$$ LANGUAGE plpgsql;
