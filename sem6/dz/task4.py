# Для натурального n создать словарь индекс-значение, состоящий из элементов
# последовательности 3n + 1. Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
checkInput = False
while not checkInput:
    try:
        num = int(input(f'Введите целое число от 3 до 10: '))
        checkInput = True if 3 <= num <= 10 else print('Сделайте корректный ввод')
    except:
        print()
        print(f'Введите число корректно')
dictResult = dict([(index, index * 3 + 1) for index in range(1, num + 1)])
print(dictResult)

