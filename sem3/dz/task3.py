# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

myList = [2.23, 5.32, 5.9, 2.07, 4.0]
print(myList)
min = myList[0] % 1 
max = min
for item in myList:
    fractional = item % 1
    if(fractional > 0):
        if fractional < min:
            min = fractional
        if fractional > max:
            max = fractional
print(round(abs(max) - abs(min), 14))