def factorial(n):
    factorial = 1
    while n > 1:
        factorial *= n
        n -= 1
    print(factorial)
if __name__ == "__main__":
    factorial(7)
