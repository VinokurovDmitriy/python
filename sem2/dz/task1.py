# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

def convertFloatToInt(num):   #перемещение точки пока не исчезнет дробная часть
    count = 1
    n = num
    while not int(n) == n:
        n = num * 10 ** count
        count += 1
    return int(n)

def printSumNumbers(num):   #подсчет и печать суммы цифр
    sum = 0
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
