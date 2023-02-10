# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел.
# 2 2
# 4

# Очистка терминала.
import os

os.system("cls")
# Ввод данных.
a = int(input('Enter A number: '))
b = int(input('Enter number B: '))


# Основнвя функция суммирования.
def num_summ(a, b):
    a += b
    return a


# Вывод данных.

print(num_summ(a, b))
