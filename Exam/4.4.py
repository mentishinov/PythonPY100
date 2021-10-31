if __name__ == "__main__":
    N = 51
    list_ = [
        i for i in range(10, N + 1) if i % 2 != 0 and i % 5 == 0
          ]
    print(list_)