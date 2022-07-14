# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

def convertFloatToInt(num):   #перемещение точки пока не исчезнет дробная часть
    roundCount = 12
    while (round(num % 1, roundCount)) > 0:
        roundCount -=1
        num = int(num) * 10 + round(num % 1, roundCount) * 10
    return int(num)

def printSumNumbers(num):   #подсчет и печать суммы цифр
    sum = 0
    leftPart = ''
    while num  > 0:
        sum += num % 10
        num = num // 10
    print(sum)
    
checkInput = False
while not checkInput:
    try:
        n = float(input('Введите вещественное число: '))
        checkInput = True 
    except:
        print('Введите  вещественное число корректно')
        
printSumNumbers(convertFloatToInt(n))
