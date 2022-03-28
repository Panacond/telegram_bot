import sqlite3
con = sqlite3.connect('example.db')
cur = con.cursor()
table = "new"
"(date text, trans text, symbol text, qty real, price real)"
# for row in cur.execute(f'SELECT * FROM {table} where date LIKE "200[9]-%"' ):
#         print(row)

for row in cur.execute(f'SELECT * FROM {table}' ):
    print(row)

cur.execute(f"update {table} set trans = 'READ' where trans='BUY'")

for row in cur.execute(f'SELECT * FROM {table}' ):
    print(row)

# cur.execute(f"drop table {table}")


# cur.executescript(f"""create view new1 AS
# select qty * price as result 
# from {table}
# """)

for row in cur.execute(f"select * from new1"):
    print(row)

for row in cur.execute(f'SELECT * FROM {table}' ):
    print(row)

con.commit()

con.close()