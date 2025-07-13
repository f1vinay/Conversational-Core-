import sqlite3

def num_tokens_from_messages(messages):
    return sum(len(m.get("content", "").split()) for m in messages)  # Approximation

def log_to_db(prompt_tokens, completion_tokens, cost, latency):
    conn = sqlite3.connect("telemetry.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS telemetry (
            id INTEGER PRIMARY KEY,
            prompt_tokens INTEGER,
            completion_tokens INTEGER,
            cost REAL,
            latency_ms INTEGER,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    cursor.execute("""
        INSERT INTO telemetry (prompt_tokens, completion_tokens, cost, latency_ms)
        VALUES (?, ?, ?, ?)
    """, (prompt_tokens, completion_tokens, cost, latency))
    conn.commit()
    conn.close()
