n = 10 # км в день
x = 5 # дней
p = 50 # % увеличения нормы
t = 0
a = 1
while a <= x:
    print('День', a, ":")
    print(n, 'км')
    t += n
    n += n * p/100
    a += 1
print('Всего за', x, 'дн. спортсмен пробежал', t, 'км')