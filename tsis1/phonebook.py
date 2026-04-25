import csv
from connect import connect


# ---------------- ADD CONTACT ----------------
def add_contact(conn):
    name = input("Name: ")
    email = input("Email: ")
    birthday = input("Birthday (YYYY-MM-DD): ")

    with conn.cursor() as cur:
        cur.execute("""
            INSERT INTO contacts(name, email, birthday)
            VALUES (%s, %s, %s)
            RETURNING id
        """, (name, email, birthday))
        contact_id = cur.fetchone()[0]

    conn.commit()
    print("Contact added:", contact_id)


# ---------------- ADD PHONE (PROCEDURE) ----------------
def add_phone(conn):
    name = input("Contact name: ")
    phone = input("Phone: ")
    ptype = input("Type (home/work/mobile): ")

    with conn.cursor() as cur:
        cur.execute("CALL add_phone(%s, %s, %s)", (name, phone, ptype))

    conn.commit()
    print("Phone added")


# ---------------- MOVE TO GROUP (PROCEDURE) ----------------
def move_group(conn):
    name = input("Contact name: ")
    group = input("Group name: ")

    with conn.cursor() as cur:
        cur.execute("CALL move_to_group(%s, %s)", (name, group))

    conn.commit()
    print("Group updated")


# ---------------- SEARCH ----------------
def search(conn):
    q = input("Search: ")

    with conn.cursor() as cur:
        cur.execute("SELECT * FROM search_contacts(%s)", (q,))
        rows = cur.fetchall()

    for r in rows:
        print(r)


# ---------------- FILTER BY GROUP ----------------
def filter_by_group(conn):
    group = input("Group: ")

    with conn.cursor() as cur:
        cur.execute("""
            SELECT c.name, c.email, g.name
            FROM contacts c
            JOIN groups g ON c.group_id = g.id
            WHERE g.name = %s
        """, (group,))
        for r in cur.fetchall():
            print(r)


# ---------------- SORT ----------------
def sort_contacts(conn):
    field = input("Sort by (name/birthday/created_at): ")

    if field not in ["name", "birthday", "created_at"]:
        field = "name"

    with conn.cursor() as cur:
        cur.execute(f"SELECT * FROM contacts ORDER BY {field}")
        for r in cur.fetchall():
            print(r)


# ---------------- PAGINATION ----------------
def paginate(conn):
    limit = 3
    offset = 0

    while True:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT * FROM contacts
                ORDER BY id
                LIMIT %s OFFSET %s
            """, (limit, offset))
            rows = cur.fetchall()

        for r in rows:
            print(r)

        cmd = input("[next / prev / quit]: ")

        if cmd == "next":
            offset += limit
        elif cmd == "prev" and offset > 0:
            offset -= limit
        elif cmd == "quit":
            break


# ---------------- CSV IMPORT ----------------
def import_csv(conn, filename="contacts.csv"):
    with open(filename, "r") as file:
        reader = csv.DictReader(file)

        with conn.cursor() as cur:
            for row in reader:
                name = row["name"]
                email = row["email"]
                birthday = row["birthday"]
                group = row["group"]
                phone = row["phone"]
                ptype = row["type"]

                # check contact
                cur.execute("SELECT id FROM contacts WHERE name=%s", (name,))
                contact = cur.fetchone()

                if not contact:
                    cur.execute("""
                        INSERT INTO contacts(name, email, birthday)
                        VALUES (%s, %s, %s)
                        RETURNING id
                    """, (name, email, birthday))

                    contact_id = cur.fetchone()[0]

                    # group handling
                    cur.execute("SELECT id FROM groups WHERE name=%s", (group,))
                    g = cur.fetchone()

                    if not g:
                        cur.execute("INSERT INTO groups(name) VALUES (%s)", (group,))
                        cur.execute("SELECT id FROM groups WHERE name=%s", (group,))
                        g = cur.fetchone()

                    group_id = g[0]

                    cur.execute("""
                        UPDATE contacts
                        SET group_id=%s
                        WHERE id=%s
                    """, (group_id, contact_id))

                else:
                    contact_id = contact[0]

                # add phone
                cur.execute("""
                    INSERT INTO phones(contact_id, phone, type)
                    VALUES (%s, %s, %s)
                """, (contact_id, phone, ptype))

        conn.commit()

    print("CSV imported successfully")


# ---------------- MENU ----------------
def menu():
    conn = connect()

    while True:
        print("""
        1. Add contact
        2. Add phone
        3. Move group
        4. Search
        5. Filter by group
        6. Sort contacts
        7. Pagination
        8. Import CSV
        0. Exit
        """)

        choice = input("Choose: ")

        if choice == "1":
            add_contact(conn)
        elif choice == "2":
            add_phone(conn)
        elif choice == "3":
            move_group(conn)
        elif choice == "4":
            search(conn)
        elif choice == "5":
            filter_by_group(conn)
        elif choice == "6":
            sort_contacts(conn)
        elif choice == "7":
            paginate(conn)
        elif choice == "8":
            import_csv(conn)
        elif choice == "0":
            break

    conn.close()


if __name__ == "__main__":
    menu()