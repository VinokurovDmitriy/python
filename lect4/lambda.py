def calk(op, a, b):
    print(op(a, b))


calk(lambda x, y: x + y, 4, 5)


def sum(a, b):
    return a + b


list_test = [(i, sum(i, i)) for i in range(1, 21) if i % 2 == 0]
print(list_test)

with open('test.txt', 'r') as f:
    str_file = f.read()
list2 = list(map(lambda x: (x, x ** 2), filter(lambda x: not x % 2, map(int, str_file))))
print(list2)

listUsers = ['peta', 'vasia', 'lisa', 'nina']
listIds = [1, 2, 3, 8]
test_zip = zip(listUsers, listIds)
print(list(test_zip))
