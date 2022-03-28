import sqlite3

source = sqlite3.connect('existing_db.db')
con = sqlite3.connect(':memory:')
source.backup(con)

cur = con.cursor()
# cur.execute('''create table stocks
# (date text, trans text, symbol text,
#  qty real, price real)''')
cur.execute("""insert into stocks
            values ('2006-01-05','BUY','RHAT',100,35.14)""")
cur.execute("""insert into stocks
            values ('2006-01-06','SELL','RHAT',50,12.24)""")
con.commit()
cur.close()

con.row_factory = sqlite3.Row
cur = con.cursor()
cur.execute('select * from stocks')

r = cur.fetchone()
print(type(r))
print(tuple(r))
print(len(r))
print(r[2])
print(r['qty'])

for member in r:
    print(member)