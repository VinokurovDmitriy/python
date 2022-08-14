import sqlite3

from dataBase.data.sql_lite_data.orders_controller import add_order

conn = sqlite3.connect('items.db')
cur = conn.cursor()


def get_item(item_id):
    request = f'SELECT * FROM goods WHERE id={item_id};'
    cur.execute(request)
    return cur.fetchone()


def add_item(item):
    cur.execute("INSERT INTO items VALUES(?, ?, ?, ?);", item)
    conn.commit()


def by_item(user_id, item_id):
    count = get_item(item_id)[3]
    if count == 0:
        return 'Данный товар закончился'
    else:
        request = f'UPDATE goods SET count = count - 1 WHERE id = {item_id};'
        cur.execute(request)
        conn.commit()
        order = (user_id, item_id, count)
        add_order(order)
