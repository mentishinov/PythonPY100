a = int(input('Введите а: '))
cond_1 = a % 2 == 0
cond_2 = a % 3 == 0
result = cond_1 or cond_2
if result:
    print('а кратно двум или трем')
else:
    print('а НЕ кратно двум или трем')
