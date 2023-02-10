# Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

# Очистка терминала.
import os

os.system("cls")
# Ввод данных.
number = int(input('Enter the number: '))
degree = int(input('Enter number degree: '))


# Основнвя функция возведение в степень через временную не изменяемую переменную.
def exponentiation(number, degree):
    temp = number
    while degree > 1:
        number = temp * number
        degree -= 1
    return number, degree


# Объявление функции и вывод данных.
n = exponentiation(number, degree)
print(n[0])
