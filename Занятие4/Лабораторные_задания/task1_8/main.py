if __name__ == "__main__":
    list_ = [4, -1, 10, -1, 3, -3, -6, 8, 6, 9]

    def make_a_list(list_random):
        return [i ** 3 if i > 0 else 0 for i in list_random]

    print(make_a_list(list_))

# if __name__ == "__main__":
#     def make_a_list(i):
#         return [i for i in range(n, m + 1) if i > sum((range(n, m + 1)))/len((range(n, m + 1)))]
#
#     n = 10
#     m = 20
#     print(make_a_list(n))
