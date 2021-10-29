if __name__ == "__main__":

    matrix = [
        [i * j for j in range(1,10)]
        for i in range(1,10)
    ]

    for row in range(1,10):
        for col in range(1,10):
            print(f"{row * col:2}", end=" ")
        print()

