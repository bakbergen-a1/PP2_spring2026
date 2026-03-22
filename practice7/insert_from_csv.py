import psycopg2
import csv

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="12345"
)
cur = conn.cursor()

with open("practice7/data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        cur.execute(
            "INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
            (row[0], row[1])
        )
cur.execute("SELECT * FROM phonebook")
rows = cur.fetchall()

for row in rows:
    print(row)
conn.commit()
print("✅ Data loaded from CSV!")
cur.close()
conn.close()