import sqlite3


def connected():
    db = "src/database/Tracker.db"
    conn = sqlite3.connect(db)
    cursor = conn.cursor()

    table = "Tracker"
    cursor.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table,)
    )
    table_exists = cursor.fetchone() is not None
    if not table_exists:
        cursor.execute(
            f"""
                CREATE TABLE {table} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                amount REAL NOT NULL,
                time DATETIME DEFAULT CURRENT_TIMESTAMP
            );
        """
        )
    return conn
