x = int(input('Введите число: '))
money = {64 : 0, 32 : 0, 16 : 0, 8 : 0, 4 : 0, 2 : 0, 1 : 0}
for bill in money:
    if x // bill != 0:
        money[bill] += x // bill
        x -= (x // bill) * bill
print(money)