--Create the patients Table 

CREATE TABLE patients(
             patient_id SERIAL PRIMARY KEY NOT NULL,
             full_name varchar(80)NOT NULL,
			 birth_date DATE NOT NULL,
			 phone_number VARCHAR(12) UNIQUE,
			 medical_history VARCHAR(70),
			 insurance_provider VARCHAR(70),
			 first_appointment DATE NOT NULL,
			 loyalty_pass VARCHAR(7) CHECK (loyalty_pass IN('Not yet', 'Owned')) NOT NULL
			 );


--Create the Treatments table 

CREATE TABLE treatments (
             treatment_num SERIAL PRIMARY KEY NOT NULL,
			 treatment_name Varchar(120) NOT NULL,
			 category VARCHAR(50),
			 duration TIMESTAMP,
			 fee Numeric (3, 12) NOT NULL
);

/* Every Patient get his treatment at his appointment,
So we create an appointments table to link the patients and the treatments tables */ 

CREATE TABLE appointment (
             appointment_num SERIAL PRIMARY KEY NOT NULL,
			 patient_id SERIAL REFERENCES patients(patient_id)  /* A patient can get many appointments
			 ON UPDATE CASCADE,                                    so the relationship is going to be one-to-many */         
			 treatment_num SERIAL REFERENCES treatments(treatment_num) -- As well as one treatment can be used for many appointments
			 ON UPDATE CASCADE,
			 time TIMESTAMP,
			 status VARCHAR(9) CHECK (status IN('Pending', 'Confirmed', 'Completed')),
			 appointment_date DATE
);

-- Last but not least, we create the billing table that is linked to appointments

create table Billing (
billing_num serial primary key,
appointment_num int references appointments(appointment_num), -- Each Invoice Updated after next appointment
fee money,
sales_tax Numeric (3, 2),
insurance_provider varchar(60),
outstanding_balance Numeric (12, 3),
amount_required Numeric (12, 3), 
payment_date Date
);

