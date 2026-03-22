import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="12345"
)
cur = conn.cursor()

name = input("Enter name: ")
phone = input("Enter phone: ")

cur.execute(
    "INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
    (name, phone)
)

conn.commit()
print("✅ Inserted!")

cur.close()
conn.close()