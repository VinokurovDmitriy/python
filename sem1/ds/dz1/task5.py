# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
def printInvite(param):
    return int(input(f'Введите {param}: '))
def printDistance(x1, y1, x2, y2):
    text = f'расстояние между точкой А({x1}, {y1}) и точкой В({x2}, {y2}) равно '
    distance = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
    print(text + str(round(distance, 2)))
checkInput = False
while not checkInput:
    try:
        pointParam = 'координату х точки А'
        xa = printInvite(pointParam)
        pointParam = 'координату y точки А'
        ya = printInvite(pointParam)
        pointParam = 'координату x точки B'
        xb = printInvite(pointParam)
        pointParam = 'координату y точки B'
        yb = printInvite(pointParam)
        checkInput = True 
    except:
        print('Введите корректно ' + pointParam)
printDistance(xa, ya, xb, yb)
    
    