--detect any ungranted lock that prevents or slows query response
SELECT 
     pid,
	 mode,
	 relation::regclass AS locked_table,
	 transactionid,
	 granted
FROM 
   pg_locks
WHERE 
     NOT granted;
