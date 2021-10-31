# array = [1, 2, 3, 44, 114]
# a = 4
# b = 1
# for i in range(len(array)):
#     if array[i] % 2 == 0:
#             array[i] = array[i] + a
#     else:
#         array[i] = array[i] - b
# print (array)

if __name__ == "__main__":

    lst_ = [1, 2, 23, 44, 114]
    a = 4
    b = 1
    new_list_1 = [
        lst_[i] + a if lst_[i] % 2 == 0 else lst_[i]
        for i in range(len(lst_))
    ]
    new_list_2 = [
        new_list_1[i] - b if i % 2 == 0 else new_list_1[i]
        for i in range(len(new_list_1))
    ]

    print(new_list_2)

