# . Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. В качестве символа-разделителя используйте пробел.

# from random import randint


# a = int(input("Введите кол-во чисел в списке"))
# list1 = []

# for i in range (a):
#     f = randint(-a,a)
#     list1.append(f)
# print(list1)
# print(f'Минимум {min(list1)} и макс. {max(list1)}')

#####################################################################################


# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:

# 1) с помощью математических формул нахождения корней квадратного уравнения

# 2) с помощью дополнительных библиотек Python


# 1)

# D = b2 − 4ac. А вот свойства дискриминанта:

# если D < 0, корней нет;
# если D = 0, есть один корень;
# если D > 0, есть два различных корня. 

# a = int(input("Введите число"))
# b = int(input("Введите число"))
# c = int(input("Введите число"))

# d = (b**2) -4*a*c
# if d < 0 :
#     print("нет корней")
# elif d == 0 :
#     x = (-b)/(4*a*c)
#     print("один корень {x}")
# elif d > 0 :
#     x =
  
#альтернативное решение 

# def discriminant(a, b, c):
#     return b ** 2 - 4 * a * c


# def solve_quadratic(a, b, c):
#     if a == 0:
#         raise ValueError("Not quadratic equation")

#     d = discriminant(a, b, c)
#     if d < 0:
#         return "No roots"
#     elif d == 0:
#         return f"One root x = {-b / (2 * a)}"
#     else:
#         x1 = (-b + d ** 0.5) / (2 * a)
#         x2 = (-b - d ** 0.5) / (2 * a)
#         return f"Two roots: x1 = {x1}, x2 = {x2}"

# if __name__ == "__main__":
#     print(solve_quadratic(5, -9, -2))
#     print(solve_quadratic(1, -4, 4))
#     print(solve_quadratic(1, -5, 9))
# print(solve_quadratic(0, 1, 2))