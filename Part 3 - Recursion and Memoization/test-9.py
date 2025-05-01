"""
Функция tribonacci()
Последовательность Трибоначчи – последовательность натуральных чисел, где каждое последующее число является суммой трех предыдущих:
1, 1, 1, 3, 5, 9, 17, 31, 57, 105 …
Реализуйте функцию tribonacci() с использованием рекурсии и мемоизации, которая принимает один аргумент:
n — натуральное число
Функция должна возвращать n-й член последовательности Трибоначчи.
"""

cache = {1: 1, 2: 1, 3: 1}


def tribonacci(n):
    result = cache.get(n)
    if result is None:
        result = tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)
        cache[n] = result
    return result


print(tribonacci(1))  # 1
print(tribonacci(7))  # 17
