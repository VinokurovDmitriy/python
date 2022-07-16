import math
# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

myList = [5, 2, 3, 6, 5, 4, 7]
myList2 = [3, 5, 6, 2, 3, 7]
def printResult(list):
    print(list)
    for index in range(0,  math.ceil(len(list) / 2)):
        print(list[index] * list[len(list) - 1 - index], end = ' ')
    print()
    print()
printResult(myList)
printResult(myList2)
        
        

    