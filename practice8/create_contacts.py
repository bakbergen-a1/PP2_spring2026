import psycopg2
from config import DB_CONFIG

conn = psycopg2.connect(**DB_CONFIG)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS contacts (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    phone VARCHAR(20)
);
""")


contacts = [
    ("Aigerim", "87001112233"),
    ("Arman", "87002223344"),
    ("Dina", "87003334455"),
    ("Nursultan", "87004445566"),
    ("Amina", "87005556677"),
    ("Bekzat", "87006667788"),
    ("Saule", "87007778899"),
    ("Timur", "87008889900"),
    ("Zhanar", "87009990011"),
    ("Aidana", "87001001122"),
]


for name, phone in contacts:
    cur.execute("""
    INSERT INTO contacts (name, phone)
    VALUES (%s, %s)
    ON CONFLICT (id) DO NOTHING;
    """, (name, phone))


conn.commit()
cur.close()
conn.close()

print("✅")