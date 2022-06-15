import sqlite3
conn=sqlite3.connect('bootcamp.db')
'''
alter table name add coloum cname dt constraint
'''
query='''
      alter table participant add colum study text not null
      '''
conn.execute(query)

conn.commit()
conn.close()