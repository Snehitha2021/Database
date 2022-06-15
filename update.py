import sqlite3
conn=sqlite3.connect('bootcamp.db')

query='''
      update participant set name='minnu' where gid=108
      '''
conn.execute(query)

print(conn.total_changes)
conn.commit()
conn.close()