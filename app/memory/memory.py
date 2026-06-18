from app.memory.database import conn, cursor

def save_memory(key, value):

    cursor.execute(
        """
        INSERT OR REPLACE INTO memory
        (key, value)
        VALUES (?, ?)
        """,
        (key, value)
    )

    conn.commit()


def get_memory(key):

    cursor.execute(
        """
        SELECT value
        FROM memory
        WHERE key=?
        """,
        (key,)
    )

    result = cursor.fetchone()

    if result:
        return result[0]

    return None


def get_all_memory():

    cursor.execute(
        """
        SELECT key, value
        FROM memory
        """
    )

    rows = cursor.fetchall()

    return dict(rows)