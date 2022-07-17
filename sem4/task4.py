checkInput = False
while not checkInput:
    try:
        n = int(input('Введите целое число: '))
        checkInput = True 
    except:
        print('Введите целое число корректно')
with open('file.txt', 'a', encoding='utf-8') as file:
    for num in range(0, n + 1):
        file.write(str(num))