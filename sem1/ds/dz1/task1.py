# Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, 
# является ли этот день выходным.

def checkWeekends(numDay):
        result = 'Да' if numDay in range(6, 8) else 'Нет'
        print(result)
day = 0
while day not in range(1, 8):
    try:
        day = int(input('Введите номер дня недели: '))
        checkWeekends(day)
    except:
        print('Введите цифру от 1 до 7')

    
    

