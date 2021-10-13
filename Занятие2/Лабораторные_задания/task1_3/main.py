A = int(input('Введите А: '))
B = int(input('Введите B: '))
sum_kv = A ** 2 + B ** 2
kv_sum = (A + B) ** 2
if sum_kv > kv_sum:
    print("Сумма квадратов больше квадрата суммы")
else:
    print('Квадрат суммы больше суммы квадратов')
