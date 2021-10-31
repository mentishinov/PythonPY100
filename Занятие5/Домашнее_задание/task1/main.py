if __name__ == "__main__":
    n = 7
    matrix = [
        [i * j for j in range(1, n+1)]
        for i in range(1, n+1)
    ]

    for row in range(1, n+1):
        for col in range(1, n+1):
            print(f"{row * col:2}", end=" ")
        print()

