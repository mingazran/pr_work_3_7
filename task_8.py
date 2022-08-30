number = int(input('Введите четырехзначное число: '))
x_1 = int(number // 1000)
print(x_1)
x_2 = int((number % 1000 - number % 100) / 100)
print(x_2)
x_3 = int((number % 100 - number % 10) / 10)
print(x_3)
x_4 = number % 10
print(x_4)