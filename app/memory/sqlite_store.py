import sqlite3
from datetime import datetime
import json

conn = sqlite3.connect("logs.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    format TEXT,
    intent TEXT,
    data TEXT,
    thread_id TEXT
)
""")
conn.commit()


def save_log(log: dict, agent_output: dict, thread_id: str = None): # type: ignore
    cursor.execute(
        "INSERT INTO logs (timestamp, format, intent, data, thread_id) VALUES (?, ?, ?, ?, ?)",
        (
            datetime.utcnow().isoformat(),
            log.get("format"),
            log.get("intent"),
            json.dumps(agent_output),
            thread_id,
        ),
    )
    conn.commit()


def read_logs():
    cursor.execute("SELECT * FROM logs ORDER BY id DESC")
    return cursor.fetchall()
