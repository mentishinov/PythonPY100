def task_1_6():
    a = int(input("Введите стипендию : "))
    b = int(input("Расходы : "))
    sum_stip = 0
    sum_raskh = 0
    for i in range(10):
        sum_stip += a
        sum_raskh += b
        b *= 1.03
    print("Необходимо денег : ",sum_raskh - sum_stip)

if __name__ == "__main__":
    task_1_6()