--Customize specific data to preserve sensitive information
CREATE VIEW assistant_schedule AS
SELECT 
     a.appointment_date,
	 a.time,
	 p.full_name,
	 a.status
FROM 
    appointments a
JOIN
    patients p ON a.patient_id = p.patient_id
JOIN
    treatments t ON a.treatment_ref = t.treatment_ref
WHERE 
     a.status IN('Confirmed', 'Completed')
ORDER BY 
     a.appointment_date, a.time;
