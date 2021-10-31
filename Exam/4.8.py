# array = [1, 2, 44, 114]
# for i in range(len(array)):
#     if array[i] % 10 == 4:
#             array[i] = array[i] / 2
# print (array)

from random import randint
if __name__ == "__main__":

    lst_ = [3, 2, 44, 114]

    new_list_ = [
        lst_[i] / 2 if lst_[i] % 10 == 4 else lst_[i]
        for i in range(len(lst_))
    ]
    print(new_list_)

# if __name__ == "__main__":
#
#     list_ = [
#         i ** 2 if i % 2 == 0 else -i
#         for i in range(10)
#     ]  # TODO
#     print(list_)
