--Transfer Main Data to the partitioned table 

INSERT INTO partitioned_appointments (
    appointment_num, patient_id, treatment_ref, time, status, appointment_date
)
SELECT 
    appointment_num, patient_id, treatment_ref, time, status, appointment_date
FROM 
    appointments;
