a = int(input('Введите двузначное число: '))
x = a % 10
y = a // 10
if (x == 4) or (x == 7) or (y == 4) or (y == 7):
   print('Цифра 4 или 7 входит в число')
else:
   print('Цифра 4 или 7 не входит в число')
