if __name__ == "__main__":
    def make_a_list(i):
        return [i for i in range(n, m + 1) if i > sum((range(n, m + 1)))/len((range(n, m + 1)))]

    n = 10
    m = 20
    print(make_a_list(n))