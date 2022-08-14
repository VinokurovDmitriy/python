# - найти наибольший простой делитель числа
def checkSimple(num):
    for item in range(2, num):
        if (num % item) == 0:
            return False
    return True

def findLargestPrimeDivisor(a):
    startRange = a if a > 0 else -a 
    for item in range(startRange - 1, 3, -1):
        if a % item == 0 and checkSimple(item):
            print(f'Наибольший простой делитель числа {a} это число {item}')
            return
    print(f'У числа {a} нет простого делителя')
        
checkInput = False
while not checkInput:
    try:
        n = int(input('Введите число: '))
        print(2 < n or n < -2)
        checkInput = True if (2 < n or n < -2) else print(f'У числа {n} нет простого делителя')
    except:
        print('Введите целое число корректно')
findLargestPrimeDivisor(n)