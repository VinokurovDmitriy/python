def inputUser(text=None, typeInt=True, condition=False):
    checkInput = False
    if not text:
        typeText = ('целое' if typeInt else 'вещественное') + ' число'
    else:
        typeText = text
    while not checkInput:
        try:
            num = input(f'{typeText}: ')
            n = int(num) if typeInt else float(num)
            condition = (lambda x: True if x > -1 else False) if not condition else condition
            checkInput = True if condition(n) else print('Сделайте корректный ввод')
        except:
            print()
            print(f'Введите {typeText} корректно')
    if checkInput:
        return n
