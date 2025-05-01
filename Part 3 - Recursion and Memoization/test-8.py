"""
Функция is_power()
Реализуйте функцию is_power() с использованием рекурсии, которая принимает один аргумент:
number — натуральное число
Функция должна возвращать значение True, если number является степенью числа 2, или False в противном случае.
"""


def is_power(number):
    if number == 1:
        return True
    elif number < 1:
        return False
    return is_power(number / 2)


print(is_power(512))    # True
print(is_power(15))     # False
print(is_power(1))      # True
print(is_power(100))    # False