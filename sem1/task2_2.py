try:
    a = float(input('Введите вещественное число: '))
    check = True
except:
    'Введите число корректно'
    check = False
def printFirstNum(num):
    fistNum = int((num % 1) *10)
    print(fistNum) if fistNum else print('no') 
if(check):
    printFirstNum(a)