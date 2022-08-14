# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число

checkInput = False
count = 8
while not checkInput:
    try:
        n = int(input(f'Введите целое число больше либо равное {count}: '))
        checkInput = True if n >= count else print(f'Вы ввели число меньше {count}') 
    except:
        print('Введите целое число корректно') 
positions = []  
with open('task4.txt', 'r') as f:
    for num in f:
        positions.append(int(num))

leftPartText = ''
multiple = 1
listNumbers = range(-n, n + 1)
print(listNumbers)
print()
for item in positions:
    print(item,' = ', listNumbers[item - 1])
    currentNumber = listNumbers[item - 1]
    leftPartText += str(currentNumber) + (' * ' if item != positions[len(positions) - 1] else '')
    multiple *= currentNumber
print(leftPartText, ' = ', multiple)