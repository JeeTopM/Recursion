"""
Реализуйте функцию get_all_values(), которая принимает два аргумента в следующем порядке:

nested_dicts — словарь, содержащий в качестве значений произвольные объекты или словари, которые,
    в свою очередь, так же содержат в качестве значений произвольные объекты или словари; вложенность может быть произвольной
key — хешируемый объект
Функция должна определять все значения, которые соответствуют ключу key в словаре nested_dicts и всех его вложенных словарях,
    и возвращать их в виде множества. Если ключа key нет ни в одном словаре, функция должна вернуть пустое множество.
"""


def get_all_values():
    pass

# test 1
my_dict = {
    "users": {
        "Arthur": {"grades": [4, 4, 3], "top_grade": 4},
        "Timur": {"grades": [5, 5, 5], "top_grade": 5},
    }
}
result = get_all_values(my_dict, "top_grade")
print(*sorted(result))
# answer - 4 5

# test 2
my_dict = {
    "Arthur": {"hobby": "videogames", "drink": "cacao"},
    "Timur": {"hobby": "math"},
}
result = get_all_values(my_dict, "hobby")
print(*sorted(result))
# answer - math videogames

# test 3
my_dict = {
    "Arthur": {"hobby": "videogames", "drink": "cacao"},
    "Timur": {"hobby": "math"},
}
result = get_all_values(my_dict, "top_grade")
print(len(sorted(result)))
# answer - 0
