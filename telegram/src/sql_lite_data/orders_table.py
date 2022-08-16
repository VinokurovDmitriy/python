import sqlite3


class OrderData:
    def __init__(self):
        self.conn = sqlite3.connect('teleshop.db')
        self.cur = self.conn.cursor()
        self.cur.execute("""CREATE TABLE IF NOT EXISTS orders(
           user_id INTEGER,
           good_id INTEGER,
           count INTEGER);
        """)
        self.conn.commit()



    def get_user_orders(self, user_id):
        request = f'SELECT goods.id, goods.name, goods.description, orders.count  FROM orders ' \
                  f'LEFT JOIN goods ON goods.id=orders.good_id ' \
                  f'WHERE orders.user_id = {user_id};'
        self.cur.execute(request)
        # print(result)
        return self.cur.fetchall()

    def get_all_orders(self):
        self.cur.execute('SELECT * FROM orders;')
        return self.cur.fetchall()

    def check_item_in_basket(self, user_id, good_id):
        result = self.cur.execute('SELECT * FROM orders WHERE user_id = ? AND good_id = ?;', (user_id, good_id))
        if result:
            return self.cur.fetchone()
        else:
            return False

    def add_order(self, order, count=1):
        good_id = order[1]
        user_id = order[0]
        if self.check_item_in_basket(order[0], good_id):
            request = f'UPDATE orders SET count = count + {count} WHERE good_id = {good_id};'
            self.cur.execute(request)
        else:
            self.cur.execute("INSERT INTO orders VALUES(?, ?, ?);", (user_id, good_id, count))
        self.conn.commit()

    def del_order(self, user_id, good_id):
        if self.check_item_in_basket(user_id, good_id):
            self.cur.execute("DELETE FROM orders WHERE user_id=? AND good_id=?;", (user_id, good_id))
            self.conn.commit()
            return 'Товар успешно удален из корзины'
        else:
            return 'Такого товара нет в корзине'





