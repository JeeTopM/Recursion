"""
Обычное возведение в степень
Реализуйте функцию get_pow() с использованием рекурсии, которая принимает два аргумента в следующем порядке:
a — положительное целое число
n — неотрицательное целое число
Функция должна вычислять значение a в степени n и возвращать полученный результат.
"""


def get_pow(a, n):
    if n == 0:
        return 1
    return a * get_pow(a, n - 1)


print(get_pow(5, 2))  # 25
print(get_pow(99, 0))  # 1
print(get_pow(2, 10))  # 1024
