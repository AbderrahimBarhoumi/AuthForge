--Apply Partitioning for appointments by date range

CREATE TABLE partitioned_appointments(
             appointment_num SERIAL, 
			 patient_id INT, 
			 treatment_ref TEXT,
			 time TIME,
			 status VARCHAR(20),
			 appointment_date DATE,
			 PRIMARY KEY (appointment_num, appointment_date)
) PARTITION BY RANGE (appointment_date);

--Create partitions by month range 

CREATE TABLE September2024_appointments PARTITION OF partitioned_appointments
FOR VALUES FROM ('2024-09-01') TO ('2024-09-30');

CREATE TABLE November2024_appointment PARTITION OF partitioned_appointments
FOR VALUES FROM ('2024-10-01') TO ('2024-10-31');
