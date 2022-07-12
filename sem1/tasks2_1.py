try:
    a = int(input('Введите число положительное целое: '))
    check = True
except:
    'Введите число корректно'
    check = False
def printRange(num):
    for number in range(-a, a + 1):
        print(f'{number} ')
if(check):
    printRange(a)