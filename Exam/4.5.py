# if __name__ == "__main__":
#     N = 51
#     list_ = [
#         i for i in range(-20, N + 1) if i < 0 and i % 2 != 0
#           ]
#     print(len(list_))

from random import randint

lst = [randint(-5, 5) for _ in range(10)]
print(lst)
print('Сумма нечетных: ', sum([i for i in lst if i % 2 != 0]))
negatives = [i for i in lst if i < 0]
print('Кол-во отрицательных: ', len(negatives))
mul = 1
for i in negatives:
    mul *= i
print('Произведение отрицательных: ', mul)