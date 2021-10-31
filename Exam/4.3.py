# A = -3
# N = 3
# result_ = 1
# for i in range(N):
#     result_ *= A
# print("Результат : ", result_)





def make_a_list(i):
    return [A ** i for i in range(0, N + 1)]
if __name__ == "__main__":
    A = -3
    N = 6
    print(make_a_list(A))

# def make_a_list(i):
#     return [i ** 2 for i in range(n, m + 1)]
# if __name__ == "__main__":
#     n = 10
#     m = 15
#     print(make_a_list(n))
