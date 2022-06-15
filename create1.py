import sqlite3
conn=sqlite3.connect('bootcamp.db')

'''
create table name(cname dt(size))
'''
query='''
     create table attend(gid int primary key,name not null,ap int not null)
      '''
conn.execute(query)
