Board = {7: '_', 8: '_', 9:"_", 4: '_', 5: '_', 6:"_", 1: '_', 2: '_', 3:"_"}   #Разметка доски

Players = {
'O': [],
'X': []
}


Win_rulez = {
    (7, 8, 9), #Верхняя горизонталь
    (4, 5, 6), #Средняя горизонталь
    (1, 2, 3), #Нижняя горизонталь
    (7, 5, 3), #\ линия
    (1, 5, 9), #/ линия
    (7, 4, 1), #Левая  вертикаль
    (8, 5, 2), #Средняя вертикаль
    (9, 6, 3) #Правая вертикаль
}

def print_board():
    print(f'{Board[7]} {Board[8]} {Board[9]}')
    print(f'{Board[4]} {Board[5]} {Board[6]}')
    print(f'{Board[1]} {Board[2]} {Board[3]}')

def win_check(sign):
    board_mask = set(Players[sign])
    winner = bool([True for rule in Win_rulez if len(board_mask.intersection(rule)) == 3])
    return winner


def set_cell(cell, sign):
    Board[cell] = sign
    Players[sign].append(cell)


def start():
    sign = 'X'
    step = 1
    while True:
        print_board()
        cell = input(f'\nХод {sign}, выберите [1-9] или 0 для выхода из игры: ')
        if cell == '0':
            break
        elif cell in list(map(str, range(1, 10))):
            if Board[int(cell)] == '_':
                set_cell(int(cell), sign)
            else:
                print(f'\nЯчейка уже занята, повторите ввод')
                continue
            if win_check(sign):        # Победа
                print(f'\nЗнак {sign} победитель!!!')
                print_board()
                break
            else:                      # Ничья
                if step == 9:
                    print(f'\nНет больше ходов! GAME OVER')
                    print_board()
                    break
                else:                  # - Смена знака
                    step += 1
            sign = 'O' if sign == 'X' else 'X'
        else:                          # - Если будет введено не верное число
            print('\nНеправильный ввод: возможно только [1-9] для выбора ячейки или 0 для выхода из игры.')
            continue


if __name__ == '__main__':
    print(f'\nДобро пожаловать в XO. Играйте шаг за шагом, от знака X до знака O.')
    print(f'Используйте Numpad для выбора клетки. Хорошей игры!!!\n')
    start()
