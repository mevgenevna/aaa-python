def step1():
    print(
        'Уткамаляр 🦆 решила погулять. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


def step2_no_umbrella():
    print(
        'Пошел дождь!🙀'
        'Едем домой?🏠'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return print('Gameover. Уточка не выгуляна ☹️')
    return print('Gameover. Уточка промокла и заболела ☹️Кря-Кря')


def step2_umbrella():
    print(
        'Куда пойдем?'
    )
    option = ''
    options = {'парк': True, 'бар': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return print('Congrats! Уточка выгуляна! 🎈')
    return print('Gameover. У уточки нет паспорта 🍷')


if __name__ == '__main__':
    step1()
