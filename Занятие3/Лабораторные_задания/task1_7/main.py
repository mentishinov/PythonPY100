def task_1_7():
    A = int(input("Введите стипендию : "))
    B = int(input("Расходы : "))
    S = int(input("Накопления : "))
    n = 0
    sum_stip = 0
    sum_raskh = 0
    while S + A > B:
        sum_stip += A
        sum_raskh += B
        n += 1
        B *= 1.05
    print('Cтудент сможет прожить ', n ,'мес.')


if __name__ == "__main__":
    task_1_7()
