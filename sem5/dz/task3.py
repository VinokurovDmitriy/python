from inputKeyboard import inputUser


# Создайте программу для игры в "Крестики-нолики".
def printBoard():
    for r in board:
        print('', end='')
        for item in r:
            print(f'{item}|', end='')
        print('')


cross = 'x'
null = '0'
empty = ' '
rowCount = inputUser('Введите размр доски (количество строк и столбцов) от 3 до 10',
                     True, lambda x: True if 3 <= x <= 10 else False)
row = [empty for item in range(rowCount)]
board = [list(row) for i in range(rowCount)]
print(board)
step = 0
winner = False
printBoard()
print(f'Игрок 1 играет {cross}, Игрок 2 играет {null}')

while not winner:
    print(f'-----------{step + 1} ход----------')
    player = step % 2 + 1
    symbolPlayer = cross if player == 1 else null
    print(f'Ход {player} игрока')
    row = inputUser(f'Введите ряд (число от 1 до {rowCount})', True, lambda x: True if 1 <= x <= rowCount else False)
    column = inputUser(f'Введите столбец (число от 1 до {rowCount})', True,
                       lambda x: True if 1 <= x <= rowCount else False)
    if board[row - 1][column - 1] == empty:
        board[row - 1][column - 1] = symbolPlayer
    else:
        printBoard()
        print('Эта ячейка уже занята. Выберете другую')
        continue
    checkWinner = lambda listVal: True if listVal.count(symbolPlayer) == len(listVal) else False
    diagLeft = [board[index][index] for index in range(rowCount)]
    diagRight = [board[index][len(board) - 1 - index] for index in range(rowCount)]
    rowWinner = False
    columnWinner = False
    checkEmpty = False
    for index in range(len(board)):
        col = [board[rowIndex][index] for rowIndex in range(rowCount)]
        columnWinner = checkWinner(col)
        if board[index].count(empty) > 0:
            checkEmpty = True
        rowWinner = checkWinner(board[index])
        if rowWinner or columnWinner:
            break
    if checkWinner(diagLeft) or checkWinner(diagRight) or rowWinner or columnWinner:
        print(checkWinner(diagLeft), checkWinner(diagRight), rowWinner, columnWinner)
        winner = True
        print(f'Выиграл игрок {player}')
    step += 1
    printBoard()
    if not checkEmpty:
        print('Игра закончилась в ничью. Победила дружба!')
        winner = True
