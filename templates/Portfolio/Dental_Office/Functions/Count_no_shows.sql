--This function is used to count missed appointments  
SELECT 
   DATE_TRUNC('Week', appointment_date) AS Week_start,
	 COUNT(*) AS missed_appointments
FROM 
    appointments
WHERE 
     status = 'No-Show'
GROUP BY 
        Week_start
ORDER BY 
        Week_start DESC;
