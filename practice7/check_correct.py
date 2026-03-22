import psycopg2

try:
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="12345"
    )
    print("✅ Connection successful!") 

    cur = conn.cursor()
    cur.execute("SELECT version()")
    version = cur.fetchone()
    print("PostgreSQL version:", version[0])  

    cur.close()
    conn.close()

except Exception as e:
    print("❌ Connection failed!")
    print("Error:", e)