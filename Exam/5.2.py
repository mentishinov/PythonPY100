n = int(input('КМ пробежал: '))
x = int(input('Кол-во дней: '))
y = float(input('Увеличение нормы в %: '))
km_day_1 = n
while x > 0:
    x -= 1
    n = n + (n * y / 100)
    sum_path = n + km_day_1
print('Всего пробежал', sum_path, 'км')