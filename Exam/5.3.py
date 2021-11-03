x = int(input('Введите число: '))

result = []
while x > 0:
    result.append(x % 10)
    x //= 10
result.reverse()
odds = 0
even = 0
for i in range(len(result)):
    if result[i] % 2 == 0:
        odds += 1
    else:
        even += 1
print('Четных: ', odds, 'Нечетных: ', even)






