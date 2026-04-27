-- Long running queries
SELECT TOP 5
    session_id,
    status,
    blocking_session_id,
    wait_type,
    wait_time,
    cpu_time,
    total_elapsed_time
FROM sys.dm_exec_requests
ORDER BY total_elapsed_time DESC;

-- Deadlocks (simplified)
SELECT * FROM sys.dm_tran_locks;

-- DB size
EXEC sp_spaceused;
