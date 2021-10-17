A = int(input('Введите A: '))
B = int(input('Введите B: '))
C = int(input('Введите C: '))
cond_1 = A < 45
cond_2 = B < 45
cond_3 = C < 45
if cond_1:
    if cond_2 == False and cond_3 == False:
        print('Условие выполнено')
    else:
        print('Условие не выполнено')
elif cond_2:
    if cond_1 == False and cond_3 == False:
        print('Условие выполнено')
    else:
        print('Условие не выполнено')
elif cond_3:
    if cond_1 == False and cond_2 == False:
        print('Условие выполнено')
    else:
        print('Условие не выполнено')
else:
    print('Условие не выполнено')

