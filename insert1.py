import sqlite3
conn=sqlite3.connect('bootcamp.db')

conn.execute("insert into attend values(108,'snehitha',99)")
conn.execute("insert into attend values(106,'snehi',95)")
conn.execute("insert into attend values(105,'sneh',98)")
conn.execute("insert into attend values(100,'sneha',92)")

conn.commit()
conn.close()