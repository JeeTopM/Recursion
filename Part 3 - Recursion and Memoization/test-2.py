"""
Сумма цифр
Напишите программу с использованием рекурсии, которая принимает на вход число и выводит сумму цифр этого числа.
"""


def recursive_sum(n):
    if n < 10:
        return n % 10
    return recursive_sum(n // 10) + n % 10


numb = int(input())
print(recursive_sum(numb))

# int(input(25))  # 7
# int(input(10000))  # 1
