from connect import connect

conn = connect()

with open("tsis1/schema.sql", "r") as f:
    sql = f.read()

with conn.cursor() as cur:
    cur.execute(sql)

conn.commit()
conn.close()

print("Database created")