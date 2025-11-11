--Import new patients daily
\COPY appointments(patient_id, treatment_id, appointment_date, time, appointment_status)
FROM 'C:\Users\abdou\OneDrive\Desktop\Dr_Louay.C\New_Patients.csv' WITH CSV HEADER;
