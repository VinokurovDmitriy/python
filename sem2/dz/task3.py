#Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.

checkInput = False
while not checkInput:
    try:
        n = int(input('Введите целое число: '))
        checkInput = True 
    except:
        print('Введите целое число корректно')
sum = 0
printResult = ''
for item in range(1, n + 1):
    result = round((1 + 1 / item)**item, 2)
    sum += result
    printResult += str(result) + (' + ' if item < n  else '')
print(f'{printResult}', '=', sum)