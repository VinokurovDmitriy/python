# проверить число на простоту (т.е. что число делится только на 1 и само на себя)
def checkSimple(num):
    check = True
    for item in range(2, num):
        if num % item == 0:
            check = False
            break
    print('Число ' + ('простое' if check else ' делится на ' + str(item) + ' без остатка'))
    
checkInput = False
while not checkInput:
    try:
        n = int(input('Введите число: '))
        checkInput = True if n != 0 else print('0 не является ни простым ни составным числом')
    except:
        print('Введите целое число корректно')
checkSimple(n)