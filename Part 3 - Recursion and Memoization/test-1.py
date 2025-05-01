"""
Количество цифр
Напишите программу с использованием рекурсии, которая принимает на вход число и выводит количество цифр в этом числе.
"""


def recursive_len(num):
    if num < 10:
        return 1
    return 1 + recursive_len(num // 10)


n = int(input())
print(recursive_len(n))
