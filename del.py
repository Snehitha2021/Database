import sqlite3
conn=sqlite3.connect('bootcamp.db')

print(conn.total_changes)
conn.commit()
conn.close()

conn=sqlite3.connect("bootcamp.db")
conn.execute("drop table participant")