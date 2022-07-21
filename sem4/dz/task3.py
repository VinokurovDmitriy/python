# Задайте последовательность чисел. Напишите программу, которая выведет
# список неповторяющихся элементов исходной последовательности.

myList = [1, 2, 3, 4, 3, 2, 4, 2, 6, 7, 2]
def getUniqueItems(listNums):
    double_list = []
    unique_list = []
    for item in listNums:
        if (item in unique_list) and (item not in double_list):
            double_list.append(item)
        unique_list.append(item)
    print(listNums)
    print('не повторяющиеся элементы: ', set(unique_list).difference(set(double_list)))

getUniqueItems(myList)
