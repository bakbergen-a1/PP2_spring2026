import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="12345"
)
cur = conn.cursor()

name = input("Enter name to update: ")
new_name = input("Enter new name: ")
new_phone = input("Enter new phone: ")

cur.execute(
    "UPDATE phonebook SET name=%s, phone=%s WHERE name=%s",
    (new_name, new_phone, name)
)

conn.commit()

if cur.rowcount > 0:
    print("✅ Updated!")
else:
    print("⚠ User not found")

cur.close()
conn.close()