-- Indexing the date column to speed up the query
CREATE INDEX index_appointment_date ON appointments(appointment_date);

--Indexing both the pk and status to boost data processing 
CREATE INDEX index_patient_status ON appointments(patient_id, status);

-- Partially Indexing the amount_required for unpaid patients
CREATE INDEX index_unpaid_bills ON billing(amount_required) WHERE payment_status = 'Unpaid';
