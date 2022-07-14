# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число
from audioop import mul


checkInput = False
count = 4
while not checkInput:
    try:
        n = int(input(f'Введите целое число больше либо равное {count}: '))
        checkInput = True if n >= count else print(f'Вы ввели число меньше {count}') 
    except:
        print('Введите целое число корректно')
        
f = open('sem2/dz/task4.txt', 'r') # у меня работает только если указать такой путь к файлу
positions = list(f.read())
f.close()
leftPartText = ''
multiple = 1
listNumbers = range(-n, n + 1)
for item in positions:
    currentNumber = listNumbers[int(item) - 1]
    leftPartText += str(currentNumber) + ' * '
    multiple *= currentNumber
print(leftPartText, ' = ', multiple)