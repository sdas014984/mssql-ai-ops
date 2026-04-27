import pyodbc
import os

conn_str = os.getenv("DB_CONN")

def kill_session(session_id):
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()

    cursor.execute(f"KILL {session_id}")
    conn.commit()

    return f"Killed session {session_id}"

