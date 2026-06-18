import sqlite3

conn = sqlite3.connect("agent_memory.db", check_same_thread=False)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS memory (
    key TEXT PRIMARY KEY,
    value TEXT
)
""")

conn.commit()