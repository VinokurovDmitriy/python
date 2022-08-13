import sqlite3
conn = sqlite3.connect('goods.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS goods(
   id INTEGER,
   description INTEGER,
   name TEXT,
   count INTEGER);
""")
conn.commit()

cur.execute("""CREATE TABLE IF NOT EXISTS orders(
   orderid INT PRIMARY KEY,
   userid INTEGER,
   total INTEGER);
""")
conn.commit()

cur.execute("SELECT * FROM goods;")
one_result = cur.fetchone()
print(one_result)
cur.execute(f'UPDATE goods SET count = count - 1 WHERE id = 34')
cur.execute("SELECT * FROM goods WHERE id=34;")
one_result = cur.fetchone()
print(one_result)
