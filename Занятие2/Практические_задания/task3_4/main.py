mount = int(input("Введите номер месяц: "))

if mount in [3, 4, 5]:
    print("Весна")
elif mount in [6, 7, 8]:
    print("Лето")
elif mount in range(9, 12):
    print("Осень")
elif mount in [12, 1, 2]:
    print("Зима")
