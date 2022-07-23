import random
from inputKeyboard import inputUser


# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"
def alienSwearing():
    print('%v %%44 4###2 22iii j///')
    print('Просим прощенья. Это непереводимая игра слов на нашем родном языке')


count = 2021
maxStepCount = 28
print(f'Привет землянин. Давай поиграем. На столе {count} конфета')
print(f'За ход можно взять не более {maxStepCount} конфет')
print('Если мы делаем последний ход, то Земля будет уничтожена')
print('Выберете сложность игры от 0 до 1, где 0 это легкий уровень,')
difficult = inputUser(' а 1 это это игра против нашего ИИ', True,  lambda x: True if x in range(2) else False)
print('Хаха. Твоя первая ошибка землянин. Ты выбрал игру против нашего ИИ') if difficult else print('Ты выбрал игру против самого умного представителя нашей цивилизации')
n = inputUser('Загадай число от 0 до 1. Если угадаешь то ходишь первый, если нет то первыми ходим мы', True,
              lambda x: True if x in range(2) else False)
draw = random.randint(0, 1)
lastStep = 0
if draw == n:
    alienSwearing()
    print(f'Выпало {draw}, вы угадали. Вы делаете первый ход')
    lastStep = 1
else:
    print(f'Хаха. Выпало {draw}. Наш ход первый')
while count > 0:
    print(f'--------{lastStep + 1} ход---------')
    print(f'На столе {count} конфет')
    if lastStep % 2 == 1:
        print('Ваш ход')
        step = inputUser('Выберете количество конфет', True, lambda x: True if 0 < x <= maxStepCount else False)
    else:
        print('Наш ход')
        if difficult == 0:
            step = random.randint(0, maxStepCount)
        else:
            step = maxStepCount if count % maxStepCount == 0 else count % maxStepCount
        print(f'Мы забрали {step} конфет')
    count = count - step if count - step > 0 else 0
    lastStep += 1
if lastStep % 2 == 0:
    alienSwearing()
    print('Ты победил землянин')
    print('Тебе опять повезло. Но мы снова вернемся с заданием посложнее')
else:
    print('Хаха. Ты проиграл. Земля будет унчитожена через 30 29 28...')
    print('ойой. Извиняемся. Мы забыли дома все уничтожители. Уничтожим землю когда вернемся')
    alienSwearing()
