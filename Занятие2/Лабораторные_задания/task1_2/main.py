A = int(input('Введите А: '))
B = int(input('Введите B: '))
cond_1 = A % 2 == 1
cond_2 = B % 2 == 1
result = cond_1 and cond_2
if result:
    print('Оба числа нечетные')
else:
    print('Условие не выпоняется')

