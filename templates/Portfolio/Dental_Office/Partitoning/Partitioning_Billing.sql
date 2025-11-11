--Create new partitioned billing table
CREATE TABLE partitioned_billing (
    billing_num SERIAL,
    appointment_num INT,
    fee MONEY,
    sales_tax NUMERIC (3, 2),
	insurance_provider VARCHAR(60),
    outstanding_balance NUMERIC(12, 3),
    amount_required NUMERIC (12, 3),
	payment_date DATE,
	payment_status VARCHAR(20),
    PRIMARY KEY (billing_num, payment_status)
) PARTITION BY LIST (payment_status);

--Create List partitioning goes by paid and unpaid patients
CREATE TABLE paid_status PARTITION OF partitioned_billing
FOR VALUES IN ('Paid');

CREATE TABLE unpaid_status PARTITION OF partitioned_billing
FOR VALUES IN ('Unpaid');


--Now, let's convert the Data to the partitioned form as we did before

INSERT INTO partitioned_billing (billing_num, appointment_num, fee, sales_tax,
insurance_provider, outstanding_balance, amount_required, payment_date,
payment_status)

SELECT billing_num, appointment_num, fee, sales_tax,
insurance_provider, outstanding_balance, amount_required, payment_date, 
payment_status 
FROM billing;

--Now we remove constraints or any other relation functions
ALTER TABLE billing DROP CONSTRAINT billing_pkey;
ALTER TABLE billing DROP CONSTRAINT billing_payment_status_check;

--Drop the table 
DROP TABLE billing

 --Rename the New table with the original name 
 ALTER TABLE partitioned_billing RENAME TO billing;

--Last but not least, we reset the table constraints
ALTER TABLE billing
ADD CONSTRAINT billing_payment_status_check CHECK (payment_status IN('Paid', 'Unpaid'));
ALTER TABLE
billing ADD CONSTRAINT billing_pkey PRIMARY KEY (billing_num);
