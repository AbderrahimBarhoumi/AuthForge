\COPY (
    SELECT 
        P.full_name,
        A.appointment_date,
        T.treatment_name,
        B.amount_required AS First_paid_amount,
        B.payment_status
    FROM 
        billing B
    JOIN appointments A ON B.appointment_num = A.appointment_num
    JOIN patients P ON A.patient_id = P.patient_id
    JOIN treatments T ON A.treatment_ref = T.treatment_ref
WHERE 
     B.payment_status IN('Unpaid')
	 AND A.appointment_date >= CURRENT_DATE - INTERVAL '30 days'
) TO 'C:\Users\abdou\OneDrive\Desktop\Dr_Louay.C\Billing_Summary.csv' WITH CSV HEADER;
	 

