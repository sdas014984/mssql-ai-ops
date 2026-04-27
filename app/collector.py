import pyodbc
import os

conn_str = os.getenv("DB_CONN")

def get_metrics():
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT TOP 5 session_id, status, wait_type, wait_time
    FROM sys.dm_exec_requests
    ORDER BY wait_time DESC
    """)

    rows = cursor.fetchall()

    data = []
    for row in rows:
        data.append({
            "session_id": row[0],
            "status": row[1],
            "wait_type": row[2],
            "wait_time": row[3]
        })

    return data
