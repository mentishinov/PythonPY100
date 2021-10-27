if __name__ == "__main__":
    def make_a_list(i):
        return [i ** 2 for i in range(n, m + 1) if i % 2 != 0]

    n = 10
    m = 15
    print(make_a_list(n))
