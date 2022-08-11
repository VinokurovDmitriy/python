from data import items, days


def getSchedule():
    # work_schedule = {day: "С 8:00 до 21:00" if day in days[:4] else 'Круглосуточно' for day in days}
    work_schedule = [day + (": 8:00 до 21:00" if day in days[:5] else ': Круглосуточно') for day in days]
    print(work_schedule)
    return '\n'.join(work_schedule)

def setCount(item):
    if items[item] > 1:
        items[item] -= 1


def parseItems():
    counts = ''
    for key, value in items.items():
        counts += f'{key}: {value}\n'
    return counts
