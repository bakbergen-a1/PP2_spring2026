import psycopg2
from config import DB_CONFIG

# Connect
conn = psycopg2.connect(**DB_CONFIG)
cur = conn.cursor()

# function for sql file
def run_sql_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        sql = f.read()
        cur.execute(sql)

#  create table if is not exists
cur.execute("""
CREATE TABLE IF NOT EXISTS contacts (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    phone VARCHAR(20)
);
""")

#  Launching functions and procedures
run_sql_file("practice8/functions.sql")
run_sql_file("practice8/procedures.sql")

#  Adding an example of the data
contacts = [
    ("Aigerim", "87001112233"),
    ("Arman", "87002223344"),
    ("Dina", "87003334455"),
    ("Nursultan", "87004445566"),
    ("Amina", "87005556677")
]

for name, phone in contacts:
    cur.execute("CALL add_or_update(%s,%s)", (name, phone))

# Contact search
cur.execute("SELECT * FROM search_contacts(%s)", ("Aig",))
print("Search result:", cur.fetchall())

# Page display
cur.execute("SELECT * FROM get_page(%s,%s)", (5, 0))
print("Page result:", cur.fetchall())

# Deleting one contact
cur.execute("CALL delete_user(%s)", ("Aigerim",))

# Save the changes and close the connection
conn.commit()
cur.close()
conn.close()

print("The table has been created, functions and procedures have been completed, and data has been added")