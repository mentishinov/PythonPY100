if __name__ == "__main__":
    cart = {
        "apple": 80,
        "orange": 65,
        "banana": 40
    }

    sum_ = 0
    for fruit in cart:
        sum_ += cart[fruit]
    print(sum_)

    sum(cart.values())

    sum(cart.values())
    cart.items()

    # TODO посчитать через ключи
    for fruit in cart:
        print(fruit)  # получаем значение по ключу

    # TODO посчитать через метод values
