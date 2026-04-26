import psycopg2

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="12345",
    host="localhost",
    port="5432"
)

cur = conn.cursor()


def init_db():
    cur.execute("""
    CREATE TABLE IF NOT EXISTS players(
        id SERIAL PRIMARY KEY,
        username VARCHAR(50) UNIQUE
    );
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS game_sessions(
        id SERIAL PRIMARY KEY,
        player_id INT REFERENCES players(id),
        score INT,
        level_reached INT,
        played_at TIMESTAMP DEFAULT NOW()
    );
    """)
    conn.commit()


def save_score(username, score, level):
    cur.execute("SELECT id FROM players WHERE username=%s", (username,))
    res = cur.fetchone()

    if res:
        pid = res[0]
    else:
        cur.execute("INSERT INTO players(username) VALUES(%s) RETURNING id", (username,))
        pid = cur.fetchone()[0]

    cur.execute(
        "INSERT INTO game_sessions(player_id, score, level_reached) VALUES(%s,%s,%s)",
        (pid, score, level)
    )
    conn.commit()


def get_top():
    cur.execute("""
    SELECT username, score, level_reached
    FROM game_sessions
    JOIN players ON players.id = game_sessions.player_id
    ORDER BY score DESC
    LIMIT 10
    """)
    return cur.fetchall()


def get_best(username):
    cur.execute("""
    SELECT MAX(score)
    FROM game_sessions
    JOIN players ON players.id = game_sessions.player_id
    WHERE username=%s
    """, (username,))
    res = cur.fetchone()
    return res[0] if res[0] else 0