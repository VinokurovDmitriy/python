# Задайте последовательность чисел. Напишите программу, которая выведет
# список неповторяющихся элементов исходной последовательности.

myList = [1, 2, 3, 4, 3, 2, 4, 2, 6, 7, 2]
newList = []
for index in range(len(myList)):
    check = True
    for i in range(index + 1, len(myList)):
        if myList[index] == myList[i]:
            check = False
    if check: newList.append(myList[index])
print(newList)
