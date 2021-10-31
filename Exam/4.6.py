numbers = [9, 5, 2, 5, -3, 8, 6, 9, -7]
unique_numbers = list(dict.fromkeys(numbers))
i = list(reversed(unique_numbers))
print(*unique_numbers)
print(min(unique_numbers), *i, max(unique_numbers))
