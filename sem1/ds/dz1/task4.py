# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y)

checkInput = False
while not checkInput:
    try:
        quart = int(input('Введите номер четверти: '))
        checkInput = True   
    except:
        print('Введите корректные координаты точки')
def checkLot(a):
    positiveX = 'х от 0 до бесконечности, '
    negativeX = 'х от минус бесконечности до 0, '
    negativeY = 'y от минус бесконечности до 0.'
    positiveY = 'y от 0 до бесконечности.'
    return {
               a == 1: negativeX + positiveY,
               a == 2: positiveX + positiveY,
               a == 3: positiveX + negativeY,
               a == 4: negativeX + negativeY
            }[True]
if checkInput:
    print(checkLot(quart))
        