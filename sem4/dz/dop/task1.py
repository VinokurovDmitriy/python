# Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и
# величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20
# тысяч, вывести фамилии этих сотрудников. Выполнить подсчёт средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32
wageDict = {}
ctrlValue = 20000
sum = 0
sum2 = 0
count = 0
with open('task1.txt', 'r', encoding='utf-8') as file:
    for item in file.read().splitlines():
        wage = float(item.split(' ')[1])
        sum += wage
        count += 1
        if(wage < ctrlValue):
            wageDict[item.split(' ')[0]] = wage
            sum2 += wage
listEmployee = list(wageDict.keys())
print(f'Сотрудники с окладом менее {ctrlValue}: ', listEmployee)
print('Средняя зарплата всех сотрудников: ', round(sum / count , 2))
print(
    f'Средняя зарплата сотрудников получающих зарплату менне {ctrlValue}: ',
      sum2 / len(listEmployee)
      )

