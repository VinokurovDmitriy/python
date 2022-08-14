# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# 45 -> 101101
# - 3 -> 11
# - 2 -> 10
checkInput = False
while not checkInput:
    try:
        n = int(input('Введите целое положительное число больше 0: '))
        checkInput = True if n > 0 else False 
    except:
        print('Введите  целое число корректно')
result = ''
while n > 0:
    result =  str(n % 2) + result
    n = n // 2
print(result)
