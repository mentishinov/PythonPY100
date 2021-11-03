# с предусловием
i = 10
while i >= 10 and i <= 30:
    print(i)
    i+=1
# с постусловием
i = 10
while True:
    if i >= 10 and i <= 30:
        print(i)
        i+=1
    else:
        break