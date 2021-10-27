if __name__ == "__main__":
    list_ = [4, -1, 10, -1, 3, -3, -6, 8, 6, 9]
    sr_arf = sum(list_)/len(list_)
    print([i - sr_arf for i in list_])




# if __name__ == "__main__":
#     def make_a_list(i):
#         return [i for i in range(n, m + 1) if i > sum((range(n, m + 1)))/len((range(n, m + 1)))]
#
#     n = 10
#     m = 20
#     print(make_a_list(n))