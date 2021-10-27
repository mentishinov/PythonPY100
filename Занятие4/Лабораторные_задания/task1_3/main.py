if __name__ == "__main__":
    def make_a_list(n):
        return [i for i in range(n) if i % 2 == 0]

    n = 10
    print(len(make_a_list(n)))