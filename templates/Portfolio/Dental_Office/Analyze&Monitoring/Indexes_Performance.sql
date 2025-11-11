--Monitor Indexs Performance 
SELECT 
      relname AS table,
	  seq_scan,
	  idx_scan AS index_performance,
	  n_tup_ins,
	  n_tup_upd,
	  n_tup_del
FROM  
      pg_stat_user_tables
ORDER BY 
      seq_scan;
