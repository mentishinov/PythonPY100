if __name__ == "__main__":
    list_ = [4, -1, 10, -1, 3, -3, -6, 8, 6, 9]
    list_of_even = [i for i in list_ if i % 2 == 0]
    list_of_odd = [i for i in list_ if i % 2 != 0]
    if len(list_of_even) > len(list_of_odd):
        print('Больше четных')
    elif len(list_of_even) < len(list_of_odd):
        print('Больше нечетных ')
    else:
        print('Равное количество')


    # if __name__ == "__main__":
    #     def make_a_list(i):
    #         return [i for i in range(n, m + 1) if i > sum((range(n, m + 1))) / len((range(n, m + 1)))]
    #
    #
    #     n = 10
    #     m = 20
    #     print(make_a_list(n))
