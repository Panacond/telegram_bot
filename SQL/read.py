import sqlite3
con = sqlite3.connect('example.db')
cur = con.cursor()
table = "new"
"(date text, trans text, symbol text, qty real, price real)"
for row in cur.execute(f'SELECT trans, qty FROM {table} ORDER BY date'):
    print(row)
print("---")
for row in cur.execute(f'select trans, qty from {table} ORDER BY date'):
    print(row)
print("---")
for row in cur.execute(f'SELECT * FROM {table} ORDER BY qty'):
    print(row)
    # print(len(row), end=" ")
    # print(row[2], end=" ")
    # print(row[3]*row[4])
# delete table
# cur.execute(f"drop table {table}")


for row in cur.execute(f"select * from new1"):
    print(row)
