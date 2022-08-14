from getDegree import getDegree
from inputKeyboard import inputUser
import random
# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

polynomial = ''
coefList = []
k = inputUser('степень числа ')
for key in range(k):
    coefList.append(random.randint(0, 101))
    polynomial += str(coefList[key]) + getDegree(k - 1)
    k -= 1
with open('task4.txt', 'w') as f:
    f.write(polynomial)
