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


    def check_item_in_basket(self, user_id, good_id):
        result = self.cur.execute('SELECT * FROM orders WHERE user_id = ? AND good_id = ?;', (user_id, good_id))
        if result:
            return self.cur.fetchone()
        else:
            return False

    def add_order(self,  good_id, user_id, count=1):
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



    def del_orders(self):
        self.cur.execute("DELETE FROM orders;")
        self.conn.commit()






