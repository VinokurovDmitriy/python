import sqlite3

conn = sqlite3.connect('orders.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS orders(
   user_id INTEGER,
   good_id INTEGER,
   count INTEGER);
""")
conn.commit()





