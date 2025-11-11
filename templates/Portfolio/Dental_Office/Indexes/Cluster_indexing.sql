--Create a clustered index for appointment_date 

CREATE INDEX date_index ON appointments(appointment_num);

--secondly, we are going to cluster the table using the index that we created

CLUSTER appointments USING date_index;
