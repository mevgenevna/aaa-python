# 1. Разбить число на цифры
def split_number(a):
    digits = []
    base = a
    l = 0
    while base > 0:
        result = base % 10
        digits.insert(0, result)
        base = base // 10
        l += 1
    return digits


split_number(4344)


# 2. Четный и нечетные
def odds_and_evens(some_number):
    digits = list(map(int, str(some_number)))
    l = len(digits) - 1
    odds = 0
    evens = 0
    while l >= 0:
        if digits[l] % 2 == 1:
            odds += 1
        else:
            evens += 1
        l -= 1
    return print('odds:' + str(odds) + ', evens:' + str(evens))


odds_and_evens(3400)


# 3. Развернуть список
def reverse_my(a):
    l = len(a) - 1
    b = []
    while l >= 0:
        b.append(a[l])
        l -= 1
    return b


reverse_my([3, 2, 1])


# 4. Вывести элементы первого множества, отсутствующие во втором
def difference(a, b):
    b = set(b)
    c = []
    for i in a:
        if i not in b:
            c.append(i)
    return c


difference([1, 2, 3, 7, 5], [1, 2, 3])


# 5. Убрать дубликаты
def delete_duplicates(a):
    b = []
    for i in a:
        if i not in b:
            b.append(i)
            i += 1
        else:
            i += 1
    return b


delete_duplicates([1, 2, 3, 7, 5, 5, 2, 9, 4])


# 6. Посчитать количество неуникальных элементов
def not_unique(a):
    a.sort()
    c = []
    i = 0
    while i < len(a) - 1:
        if a[i] == a[i + 1]:
            c.append(a[i])
            i += 1
        else:
            i += 1
    return len(set(c))


not_unique([1, 2, 3, 7, 5, 5, 2, 9, 4, 4, 4])


# 7. Удалить элементы неуд условию
def delete_by_condition(a):
    a.sort()
    i = 0
    while i < len(a) - 1:
        if a[i] < 7:
            a.remove(a[i])
        else:
            i += 1
    return a


delete_by_condition([1, 2, 3, 7, 5, 5, 2, 9, 4, 4])


# 8. Разбить строку на слова и посчитать входжения
def count_words(text):
    a = text.split(" ")
    d = {}

    for i in a:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d


count_words('разбить строку на слова и посчитать вхождения! слова')


# 9. заменить несколько идущих подряд пробельных символов на 1
def delete_mult_spaces(text):
    a = text.split(" ")
    while '' in a:
        a.remove('')
    # text1 = ' '.join(a)
    return ' '.join(a)


delete_mult_spaces('      заменить  пробелы на один')


# 10.  дан список строк. оставить только те, в которые входит заданная
def delete_if_not_include(a, b):
    c = []
    i = 0
    for i in a:
        if b in i:
            c.append(i)
        else:
            continue
    return c


delete_if_not_include(['один', 'дважды два', 'два', 'три'], 'два')


# 11. Дан список пар координат, вывести только те, которые заданы неверно,
# широта должна быть от -90.00 до 90, долгота от -180 до 180

def show_wrong_coordinates(a):
    c = []
    for i in a:
        if i[0] >= -90.0 and i[0] <= 90.0 and i[1] >= -180.0 and i[1] <= 180.0:
            continue
        else:
            c.append(i)
    return c


show_wrong_coordinates([[-90, 90], [105, 220], [125, 0], [0, 0]])


# 12. Найти неверно закрывающуюся скобку в выражении () ((([]))}
def find_wrong_bracket(a):
    b = a.replace(' ', '')
    c = ''
    l = len(b) - 1
    import math
    for i in range(0, math.ceil(len(b) / 2)):
        if b[i] == '(' and b[l - i] == ')' or b[i] == '[' and b[l - i] == ']' or b[i] == '{' and b[l - i] == '}':
            continue
        elif b[i] in [')', '}', ']']:
            c = b[i]
            break
        else:
            c = b[l - i]
            break
    return c


find_wrong_bracket('() ((([]))}')