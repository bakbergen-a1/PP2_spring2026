from connect import connect


conn = connect()
cur = conn.cursor()

# add user
cur.execute("CALL add_or_update(%s,%s)", ("Aigerim", "87777777777"))

# search
cur.execute("SELECT * FROM search_contacts(%s)", ("Aig",))
print(cur.fetchall())

# page
cur.execute("SELECT * FROM get_page(%s,%s)", (5, 0))
print(cur.fetchall())

# delete
cur.execute("CALL delete_user(%s)", ("Aigerim",))

conn.commit()
cur.close()
conn.close()