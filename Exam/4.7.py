from random import randint

lst = [randint(-100, 100) for _ in range(20)]
print(*set(lst))