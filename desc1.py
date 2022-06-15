import sqlite3
conn=sqlite3.connect('bootcamp.db')
'''
  desc attend
  pragma table_info(table_nmae
'''
str=conn.execute("pragma table_info('attend')")
print(str)
for i in str:
    print(i)