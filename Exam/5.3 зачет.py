# x = int(input('Введите число: '))
#
# result = []
# # while x > 0:
# #     result.append(x % 10)
# #     x //= 10
# def make_a_list(x):
#     return [list.append(x) % 10 and x // 10 for result if x > 0]
# x_n = (x % 10 ** n) // (10 ** n -1)
# result.reverse()
# odds = 0
# even = 0
# for i in range(len(result)):
#     if result[i] % 2 == 0:
#         odds += 1
#     else:
#         even += 1
# print('Четных: ', odds, 'Нечетных: ', even)
#
#
# def make_a_list(i):
#     return [i ** 2 for i in range(n, m + 1)]
# if __name__ == "__main__":
#     n = 10
#     m = 15
#     print(make_a_list(n))

if __name__ == "__main__":
    a = int(input("Ввведите число: "))
    list_a = [int(i) for i in str(a)]
    even = 0
    odd = 0
    for x in list_a:
        if x % 2 == 0:
            even += 1
        else:
            odd += 1
    print("четных: ", even)
    print("нечетных: ", odd)
