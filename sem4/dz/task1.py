from decimal import *
from inputKeyboard import inputUser
#Вычислить число pi c заданной точностью d 
def bbp(n):
    pi = Decimal(0)
    k = 0
    while k < n:
        pi += (Decimal(1)/(16**k))*((Decimal(4)/(8*k+1))-(Decimal(2)/(8*k+4))-(Decimal(1)/(8*k+5))-(Decimal(1)/(8*k+6)))
        k += 1
    return pi

d = int(inputUser('число требуемое число знаков после запятой', False))
if 0 < d <= 10:
    quant = '1.'
    for i in range(d):
        quant += '0'
    print(bbp(d).quantize(Decimal(quant), ROUND_FLOOR))
    print('На этот раз вам повезло, жалкие людишки. В следующий раз мы прилетим с более сложным заданием')
else:
    print('Вы не ввели число корректно согласно поставленному условию.')
    print('Через 30 секунд ваша жалкая планета будет уничтожена. Ха ха')
    print('Обратный отсчет до уничтожения начался: 30, 29, 28 ... ой мы сбились со счета.')
    print('Уничтожение планеты отложено до следующего некорректного ввода')
    