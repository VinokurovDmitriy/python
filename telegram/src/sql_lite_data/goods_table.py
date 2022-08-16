import sqlite3



class ItemsData:
    def __init__(self):
        self.conn = sqlite3.connect('teleshop.db')
        self.cur = self.conn.cursor()
        self.cur.execute("""CREATE TABLE IF NOT EXISTS goods(
                   id INTEGER PRIMARY KEY,
                   name TEXT,
                   description INTEGER,
                   count INTEGER);
                """)
        self.conn.commit()
        if not self.get_items():
            more_goods = [(34, 'Помидоры', 'черри', 13), (3, 'Огурцы', 'пупырчатые', 8),
                          (4, 'Баклажаны', 'синенькие', 7)]
            self.cur.executemany("INSERT INTO goods VALUES(?, ?, ?, ?);", more_goods)
            self.conn.commit()

    def get_item(self, item_id):
        request = f'SELECT * FROM goods WHERE id={item_id};' if item_id else 'SELECT * FROM goods;'
        self.cur.execute(request)
        return self.cur.fetchone()

    def get_items(self):
        self.cur.execute("SELECT * FROM goods;")
        return self.cur.fetchall()

    def get_first(self):
        self.cur.execute('SELECT * FROM goods')
        return self.cur.fetchone()

    def add_item(self, item):
        self.cur.execute("INSERT INTO items VALUES(?, ?, ?, ?);", item)
        self.conn.commit()

    def by_item(self, item_id):
        count = self.get_item(item_id)[3]
        if count == 0:
            return False
        else:
            request = f'UPDATE goods SET count = count - 1 WHERE id = {item_id};'
            self.cur.execute(request)
            self.conn.commit()
            return True
    def return_item(self, item_id, count_in_basket):
        if count_in_basket == 0:
            return False
        else:
            request = f'UPDATE goods SET count = count + 1 WHERE id = {item_id};'
            self.cur.execute(request)
            self.conn.commit()
            return True
