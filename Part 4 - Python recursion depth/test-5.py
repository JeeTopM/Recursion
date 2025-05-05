"""
Реализуйте функцию dict_travel(), которая принимает один аргумент:

nested_dicts — словарь, содержащий в качестве значений числа, строки или словари, которые, в свою очередь,
    так же содержат в качестве значений числа, строки или словари; вложенность может быть произвольной
Функция должна выводить все пары ключ-значение словаря nested_dicts, а также значения всех его дочерних словарей.
    При выводе значений дочерних словарей необходимо перечислять имена всех ключей, начиная с верхнего уровня, разделяя их точками.

Например, в словаре:
{'name': 'Arthur', 'grades': {'math': 4, 'chemistry': 3}}
значение 4 должно быть выведено в следующем формате:
grades.math: 4
Все пары ключ-значение должны быть расположены в лексикографическом порядке, каждая на отдельной строке.
"""


def dict_travel(nested_dicts, d=""):
    for k, v in sorted(nested_dicts.items()):
        if isinstance(v, dict):
            dict_travel(v, d + f"{k}.")
        else:
            print(f"{d}{k}: {v}")


# test 1
data = {"a": 1, "b": {"c": 30, "a": 10, "b": 20}}
dict_travel(data)
print()
# answer:
"""
a: 1
b.a: 10
b.b: 20
b.c: 30
"""

# test
data = {"d": 1, "b": {"c": 30, "a": 10, "b": 20}, "a": 100}
dict_travel(data)
print()
# answer:
"""
a: 100
b.a: 10
b.b: 20
b.c: 30
d: 1
"""

# test
data = {"b": {"c": 30, "a": 10, "b": {"d": 40, "e": 50}}}
dict_travel(data)
# answer:
print()
"""
b.a: 10
b.b.d: 40
b.b.e: 50
b.c: 30
"""
data = {
    "firstname": "Alyson",
    "lastname": "Hannigan",
    "birthday": {"day": 24, "month": "March", "year": 1974},
}
dict_travel(data)
