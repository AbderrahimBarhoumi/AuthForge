--First, we need to create the function logic to set the pass application 
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



/*Then we create another function that will update the patients table 
to give them the loyalty pass
*/
CREATE OR REPLACE FUNCTION update_loyalty_pass()
RETURNS VOID AS $$
BEGIN
    UPDATE patients
    SET loyalty_pass = TRUE
    WHERE patient_id IN (
        SELECT patient_id
        FROM appointments
        WHERE status = 'Completed'
        GROUP BY patient_id
        HAVING COUNT(*) > 5
    );
