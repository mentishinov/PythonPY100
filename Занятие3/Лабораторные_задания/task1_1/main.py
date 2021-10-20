def task_1_1():
    max_sum = 500
    current_sum = 0
    n = 1
    #while current_sum <= max_sum:
       # current_sum += n ** 2
        #print(n, current_sum)
        #n = n + 1
    while True:
        sqrt_n = n ** 2
        current_sum += n ** 2

        if current_sum + sqrt_n > max_sum:
            break
        current_sum <= max_sum
        print(n, current_sum)

    return n

if __name__ == "__main__":
    task_1_1()
