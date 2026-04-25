from connect import connect

def run_sql_file(cursor, filename):
    with open(filename, "r", encoding="utf-8") as f:
        sql = f.read()
        cursor.execute(sql)

def init_db():
    conn = connect()

    try:
        with conn.cursor() as cur:
           
            run_sql_file(cur, "tsis1/schema.sql")

            
            run_sql_file(cur, "tsis1/procedures.sql")

        conn.commit()
        print("Database initialized successfully!")

    except Exception as e:
        conn.rollback()
        print("Error:", e)

    finally:
        conn.close()


if __name__ == "__main__":
    init_db()