def define_field_size():
    '''Gets field size from user'''
    print('Введите размер поля от 3 до 5:')
    N = input()
    while N not in ['3', '4', '5']:
        print('Размер поля должен быть от 3 до 5:')
        N = input()
    N = int(N)
    return create_field(N)


def create_field(size):
    '''Creates field with a given size'''
    field = []
    n = 0
    while n < size:
        r = []
        field.append(r)
        i = 0
        while i < size:
            field[n].append(' ')
            i += 1
        n += 1
    return show_field(field, 1)


def show_field(f, call_player):
    '''Displays current field. If call_player = 1 causes first player turn'''
    N = len(f)
    letters = ['a', 'b', 'c', 'd', 'e']
    # header = ' '
    header = ''
    i = 1
    while i <= N:
        header = header + '  ' + str(i) + ' '
        # header += str(i)
        i += 1
    print(header)
    n = 0
    while n < N:
        row = letters[n]
        i = 0
        while i < N:
            if i == 0:
                row = row + ' ' + f[n][i]
                i += 1
            else:
                row = row + ' | ' + f[n][i]
                i += 1
        print(row)
        if n != N - 1:
            print(' ' + '-' * (4 * N - 1))
        n += 1
    if call_player == 1:
        return player1(f)


def player1(f):
    '''Gets coordinates from first user and fills cell with x'''
    N = len(f)
    options = []
    n = 1
    while n <= N:
        i = 1
        while i <= N:
            options.append(str(n) + ' ' + str(i))
            i += 1
        n += 1

    print('Ход первого игрока. Выберите свободную клетку и введите номер строки и столбца через пробел:')
    answer = input()

    while answer not in options:
        print(
            'Некорректное значение. Введите номер строки и столбца через пробел. Например: 1 2. Номер строки и столбца не может быть больше ' + str(
                N))
        answer = input()

    n, i = answer.split()
    n = int(n)
    i = int(i)
    if f[n - 1][i - 1] == ' ':
        f[n - 1][i - 1] = 'x'
        # print(f)
        show_field(f, 0)
        return checking(f, p=1)
    else:
        print('Эта ячейка занята. Попробуйте еще раз.')
        return player1(f)


def player2(f):
    '''Gets coordinates from second user and fills cell with o'''
    N = len(f)
    options = []
    n = 1
    while n <= N:
        i = 1
        while i <= N:
            options.append(str(n) + ' ' + str(i))
            i += 1
        n += 1

    print('Ход второго игрока. Выберите свободную клетку и введите номер строки и столбца через пробел:')
    answer = input()
    while answer not in options:
        print(
            'Некорректное значение. Введите номер строки и столбца через пробел. Например: 1 2. Номер строки и столбца не может быть больше ' + str(
                N))
        answer = input()
    n, i = answer.split()
    n = int(n)
    i = int(i)
    if f[n - 1][i - 1] == ' ':
        f[n - 1][i - 1] = 'o'
        # print(f)
        show_field(f, 0)
        return checking(f, p=2)
    else:
        print('Эта ячейка занята. Попробуйте еще раз.')
        return player2(f)


def checking(f, p):
    '''Checks if sb. won. Checks if there are any empty cells. Shows result'''
    N = len(f)
    # сумма по строкам
    n = 0
    while n < N:
        i = 0
        x = 0
        o = 0
        while i < N:
            if f[n][i] == 'x':
                x += 1
            elif f[n][i] == 'o':
                o += 1
            i += 1
        if x == N:
            return print('Победил первый игрок! 🎉')
            # print('Победил первый игрок! 🎉')
            break
        elif o == N:
            return print('Победил второй игрок! 🎉')
            # print('Победил второй игрок! 🎉')
            break
        else:
            n += 1

    # сумма по столбцам
    n = 0
    while n < N:
        i = 0
        x = 0
        o = 0
        while i < N:
            if f[i][n] == 'x':
                x += 1
            elif f[i][n] == 'o':
                o += 1
            i += 1
        if x == N:
            return print('Победил первый игрок! 🎉')
            # print('Победил первый игрок! 🎉')
            break
        elif o == N:
            return print('Победил второй игрок! 🎉')
            # print('Победил второй игрок! 🎉')
            break
        else:
            n += 1

    # сумма до диагоналям
    n = 0
    x = 0
    o = 0
    while n < N:
        if f[n][n] == 'x':
            x += 1
        elif f[n][n] == 'o':
            o += 1
        n += 1
    if x == N:
        return print('Победил первый игрок! 🎉')
        # print('Победил первый игрок! 🎉')
    elif o == N:
        return print('Победил второй игрок! 🎉')
        # print('Победил второй игрок! 🎉')

    n = 0
    x = 0
    o = 0
    while n < N:
        if f[N - 1 - n][n] == 'x':
            x += 1
        elif f[N - 1 - n][n] == 'o':
            o += 1
        n += 1
    if x == N:
        return print('Победил первый игрок! 🎉')
        # print('Победил первый игрок! 🎉')
    elif o == N:
        return print('Победил второй игрок! 🎉')
        # print('Победил второй игрок! 🎉')

    # проверка, что остались свободные клетки
    n = 0
    empty = 0
    while n < N:
        i = 0
        while i < N:
            if f[i][n] == ' ':
                empty += 1
            i += 1
        n += 1
    if empty == 0:
        return print('Свободных клеток больше нет. Игра закончена.')
    elif p == 1:
        return player2(f)
    elif p == 2:
        return player1(f)
    else:
        return print('Что-то пошло не так')


if __name__ == '__main__':
    define_field_size()
