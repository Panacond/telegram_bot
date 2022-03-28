import sqlite3
con = sqlite3.connect('example.db')
cur = con.cursor()

# Create table
name_table = "new"
try:
    cur.execute(f"CREATE TABLE {name_table} (date text, trans text, symbol text, qty real, price real)")
except:
    print("table create ago")
# Insert a row of data
cur.execute(f"INSERT INTO {name_table} VALUES ('2006-01-05','BUY', 'RHAT' ,100 ,35.14)")


cur.execute(f"INSERT INTO {name_table} VALUES (?, ?, ?, ?, ?)", ('2003-01-05','SELL', 'RHAT' ,70 ,25.14))

# The qmark style used with executemany():
lang_list = [
    ('2006-01-05', 'BUY', 'RHAT', 109 ,35.14),
    ('2007-01-05', 'BUY', 'RHAT', 108 ,35.14),
    ('2008-01-05', 'SELL', 'RHAT', 102 ,35.14),
    ('2009-01-05', 'BUY', 'RHAT', 104 ,35.14),
    ('2009-01-05', 'BUY', 'RHAT', 100 ,35.14),
]
cur.executemany(f"insert into {name_table} values (?, ?, ?, ?, ?)", lang_list)

# Save (commit) the changes
con.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
con.close()