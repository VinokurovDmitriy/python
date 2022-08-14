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
more_goods = [(34, 'черри', 'Помидоры', 13), (3, 'пупырчатые', 'Огурцы', 8), (4, 'синенькие', 'Баклажаны', 7)]
cur.executemany("INSERT INTO goods VALUES(?, ?, ?, ?);", more_goods)
conn.commit()
