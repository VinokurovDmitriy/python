# Напишите программу, которая принимает на вход координаты точки
# (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).

checkInput = False
while not checkInput:
    try:
        x = int(input('Введите координату х: '))
        y = int(input('Введите координату y: '))
        checkInput = True if(x != 0 or y != 0) else print('х и y не должны быть равны 0')
                
    except:
        print('Введите корректные координаты точки')
def checkQuart(x, y):
    return {
               x < 0 or y > 0: 1,
               x > 0 or y > 0: 2,
               x > 0 or y < 0: 3,
               x < 0 or y < 0: 4,
               x == 0: 'Точка лежит на оси x',
               y == 0: 'Точка лежит на оси y'}[True]
if checkInput:
    print(checkQuart(x, y))
        