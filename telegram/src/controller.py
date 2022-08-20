from loader import db
from quest import quest


def getSchedule():
    days = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']
    work_schedule = [bold_text(day) + (": 8:00 до 21:00" if day in days[:5] else ': Круглосуточно') for day in days]
    return '\n'.join(work_schedule)


def bold_text(text):
    return f'<b>{text}</b>'
def itallic_text(text):
    return f'<i>{text}</i>'


def printItem(item_data):
    text_data = f'{bold_text("Название товара:")} {item_data[1]}\n' \
                f'{bold_text("Описание:")} {item_data[2]}\n' \
                f'{bold_text("Количество:")} {item_data[3]}\n'
    return text_data

def print_quest(num_quest):
    text = f'{num_quest} вопрос:'
    return f'{bold_text(text)} {itallic_text(quest[num_quest - 1])}'

def printItems(items_data):
    return '\n'.join([printItem(item) for item in items_data])


def get_next_id(good_id, next_id=True):
    list_ids = list(map(lambda x: x[0], db.get_items()))
    index = list_ids.index(int(good_id))
    try:
        return list_ids[index + (1 if next_id else -1)]
    except:
        return list_ids[0] if next_id else list_ids[-1]


def get_id(call):
    return call.data.split(':')[-1]
