"""
Функция recursive_sum()

Реализуйте recursive_sum() с использованием рекурсии, которая принимает один аргумент:

nested_lists — список, элементами которого являются целые числа или списки, элементами которых,
    в свою очередь, также являются либо целые числа, либо списки; вложенность может быть произвольной
Функция должна вычислять сумму всех чисел во всех списках и возвращать полученный результат.
    Если список nested_lists пуст, функция должна вернуть число 0.
"""


def recursive_sum(data, res=0):
    if type(data) == int:
        res += data
    if type(data) == list:
        for i in data:
            res += recursive_sum(i)
    return res


# test 1
my_list = [1, [4, 4], 2, [1, [2, 10]]]
print(recursive_sum(my_list))
# answer - 24

# test 2
my_list = []
print(recursive_sum(my_list))
# answer - 0
