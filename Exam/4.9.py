# array = [1, 2, 3, 44, 114]
# for i in range(len(array)):
#     if array[i] % 2 == 0:
#             array[i] = array[i] ** 2
#     else:
#         array[i] = array[i] * 2
# print (array)


if __name__ == "__main__":

    lst_ = [1, 2, 3, 44, 114]

    new_list_ = [
        lst_[i] ** 2 if lst_[i] % 2 == 0 else lst_[i] * 2
        for i in range(len(lst_))
    ]
    print(new_list_)