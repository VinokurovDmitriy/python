from loader import data_manager


def getSchedule():
    days = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']
    work_schedule = [day + (": 8:00 до 21:00" if day in days[:5] else ': Круглосуточно') for day in days]
    return '\n'.join(work_schedule)


# def setCount(item):
#     if items[item] > 1:
#         items[item] -= 1


# def parseItems():
#     counts = ''
#     for key, value in items.items():
#         counts += f'{key}: {value}\n'
#     return counts


def printItem(index=0):
    status, item_info = data_manager.get_item(index)
    text_data = f'Название товара: {item_info["name"]}\n' \
           f'Количество: {item_info["count"]}\n' \
           f'Описание: {item_info["description"]}'
    return text_data
