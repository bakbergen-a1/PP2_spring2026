import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="12345"
)
cur = conn.cursor()

print("1 - Show all")
print("2 - Search by name")
print("3 - Search by phone")

choice = input("Choose: ")

if choice == "1":
    cur.execute("SELECT * FROM phonebook")

elif choice == "2":
    name = input("Enter name: ")
    cur.execute("SELECT * FROM phonebook WHERE name = %s", (name,))

elif choice == "3":
    phone = input("Enter phone: ")
    cur.execute("SELECT * FROM phonebook WHERE phone = %s", (phone,))

rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
conn.close()