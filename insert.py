import sqlite3
conn=sqlite3.connect('bootcamp.db')

conn.execute("insert into participant values(108,'snehitha','CSAI','Btech')")
conn.execute("insert into participant values(106,'snehi','CSI','Btech')")
conn.execute("insert into participant values(105,'sneh','CS','Btech')")
conn.execute("insert into participant values(100,'sneha','CAI','Btech')")

conn.commit()
conn.close()