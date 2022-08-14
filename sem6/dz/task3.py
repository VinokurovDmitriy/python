# Найти сумму чисел списка стоящих на нечетной позиции
myList = [2, 4, 1, 5, 12, 45, 56, 6, 67]
listOddPositions = [myList[index] for index in range(0, len(myList), 2)]
print(f'Исходный список: {myList}')
print(f'Список элементов стояших на нечетных позициях: {listOddPositions}')
print(f'Сумма элементов стоящих на нечетных позициях: {sum(listOddPositions)}')