#  найти факториал числа
def printFactorial(num):
    result = 1
    for item in range(1, num + 1):
        result *= item  
    print(f'Факториал числа {n} равен {result}') 
     
checkInput = False
while not checkInput:
    try:
        n = int(input('Введите число: '))
        checkInput = True if n > -1 else print('Введите положитнльное число или 0')
    except:
        print('Введите целое число корректно')
printFactorial(n)