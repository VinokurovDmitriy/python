import sqlite3

conn = sqlite3.connect('orders.db')
cur = conn.cursor()


def get_user_orders(user_id):
    request = f'SELECT * FROM orders WHERE user_id = {user_id};'
    cur.execute(request)
    return cur.fetchall()

def check_item_in_basket(user_id, item_id):
    cur.execute('SELECT * FROM orders WHERE user_id = ? AND item_id = ?;', (user_id, item_id))
    print(cur.fetchone())
    return cur.fetchone()

def add_order(order):
    item_id = order[1]
    if check_item_in_basket(order[0], item_id):
        request = f'UPDATE orders SET count = count + 1 WHERE id = {item_id};'
        cur.execute(request)
    else:
        cur.execute("INSERT INTO orders VALUES(?, ?, ?);", order)
    conn.commit()

def del_order(user_id, item_id):
    if check_item_in_basket(user_id, item_id):
        cur.execute("DELETE FROM orders WHERE user_id=? AND item_id=?;", (user_id, item_id))
        conn.commit()
        return 'Товар успешно удален из корзины'
    else:
        return 'Такого товара нет в корзине'

