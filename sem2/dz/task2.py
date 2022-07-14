# Напишите программу, которая принимает на вход число N 
# и выдает набор произведений чисел от 1 до N.
checkInput = False
while not checkInput:
    try:
        n = int(input('Введите целое число: '))
        checkInput = True 
    except:
        print('Введите целое число корректно')

for i in range(1, n + 1):
    multiple = 1
    for j in range(1, i + 1):
        multiple *= j
    print(f'{multiple}', end = ' ')