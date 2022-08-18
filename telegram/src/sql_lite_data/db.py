import sqlite3


class DB:
    def __init__(self):
        self.conn = sqlite3.connect(r'sql_lite_data/db/telebot.db')
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
        self.cur.execute("""CREATE TABLE IF NOT EXISTS orders(
                   user_id INTEGER,
                   good_id INTEGER,
                   count INTEGER);
                """)
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

    def get_user_orders(self, user_id):
        request = f'SELECT goods.id, goods.name, goods.description, orders.count  FROM orders ' \
                  f'LEFT JOIN goods ON goods.id=orders.good_id ' \
                  f'WHERE orders.user_id = {user_id};'
        self.cur.execute(request)
        return self.cur.fetchall()

    def check_item_in_basket(self, user_id, good_id):
        result = self.cur.execute('SELECT * FROM orders WHERE user_id = ? AND good_id = ?;', (user_id, good_id))
        if result:
            return self.cur.fetchone()
        else:
            return False

    def add_order(self, good_id, user_id, count=1):
        if self.check_item_in_basket(user_id, good_id):
            request = f'UPDATE orders SET count = count + {count} WHERE good_id = {good_id};'
            self.cur.execute(request)
        else:
            self.cur.execute("INSERT INTO orders VALUES(?, ?, ?);", (user_id, good_id, count))
        self.conn.commit()

    def return_order(self, good_id, user_id, count=1):
        if self.check_item_in_basket(user_id, good_id):
            request = f'UPDATE orders SET count = count - {count} WHERE good_id = {good_id};'
        else:
            request = f'DELETE FROM orders WHERE good_id={good_id} and user_id={user_id};'
        self.cur.execute(request)
        self.conn.commit()

    def del_orders(self, user_id):
        self.cur.execute(f'DELETE FROM orders WHERE user_id={user_id};')
        self.conn.commit()
