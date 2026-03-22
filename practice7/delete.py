import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="12345"
)
cur = conn.cursor()

print("1 - Delete by name")
print("2 - Delete by phone")

choice = input("Choose: ")

if choice == "1":
    name = input("Enter name: ")
    cur.execute("DELETE FROM phonebook WHERE name=%s", (name,))

elif choice == "2":
    phone = input("Enter phone: ")
    cur.execute("DELETE FROM phonebook WHERE phone=%s", (phone,))

conn.commit()

if cur.rowcount > 0:
    print("✅ Deleted!")
else:
    print("⚠ Not found")

cur.close()
conn.close()