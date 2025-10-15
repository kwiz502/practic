#Ввести 2 числа. Если их произведение отрицательно, умножить его на 8, в противном случае увеличить его в 1.5 раза.
a = input('Введите первое число: ')
b = input('Введите второе число: ')
while type(a) != int: # обработка исключений
  try:
    a = int(a)
  except ValueError:
    print("Неправильно ввели!")
    a = input("Введите число: ")
while type(b) != int: # обработка исключений
  try:
    b = int(b)
  except ValueError:
    print("Неправильно ввели!")
    b = input("Введите число: ")
if (a * b) < 0:
    print(a * b * 8)
else:
    print(a * b * 1,5)