if __name__ == "__main__":
    def make_a_list(i):
        return [i for i in range(a, b + 1)]

    a = 10
    b = 15
    N = len(make_a_list(a))
    print(make_a_list(a),'Количество чисел: ', N)
