if __name__ == "__main__":
    list_ = [4, -1, 10, -1, 3, -3, -6, 8, 6, 9]

    # предположим, что первый элемент в нашем списке минимальный
    min_value = list_[0]

    # а далее пройдемся по всему списку, и будем искать элемент меньший ранее найденного минимального значения
    for current_value in list_:  # TODO где будем перебирать?
        # если текущее значение меньше минимума, то перезаписываем минимум
        print("Текущее минимальное значение", min_value)
        print("Текущий элемент", current_value)
        # если нашли элемент меньше ранее найденного минимума, то перезаписываем его
        if current_value < min_value:  # TODO записать условие
            print("Найден элемент меньший минимума")
            min_value = current_value

        print("-" * 10)

    # после того как пройдем по всему списку, напечатаем список и  минимальный элемент
    print(list_)
    print("Минимальный элемент =", min_value)
