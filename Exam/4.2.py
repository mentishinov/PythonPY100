if __name__ == "__main__":
    def make_a_list(i):
        return [i for i in range(a + 1, b)]

    a = 10
    b = 15
    N = len(make_a_list(a))
    print(list(reversed(make_a_list(b))),'Количество чисел:', N)
