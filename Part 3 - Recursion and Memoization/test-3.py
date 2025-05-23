"""
Функция number_of_frogs()
В первый год в пруду живет 77 лягушек. Каждый год из пруда вылавливают 30 лягушек,
а оставшиеся размножаются, и их становится в три раза больше.
Реализуйте функцию number_of_frogs() с использованием рекурсии, которая принимает один аргумент:
year — натуральное число
Функция должна возвращать единственное число — количество лягушек в пруду в году year.
"""


def number_of_frogs(year):
    if year == 1:
        return 77
    return 3* (number_of_frogs(year - 1) - 30)


print(number_of_frogs(2))  # 141
print(number_of_frogs(10))  # 629901
