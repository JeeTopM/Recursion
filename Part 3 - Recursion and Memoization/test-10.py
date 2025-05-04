"""
Функция is_palindrome()
Реализуйте функцию is_palindrome() с использованием рекурсии, которая принимает один аргумент:
string — произвольная строка
Функция должна возвращать значение True, если переданная строка является палиндромом, или False в противном случае.
"""


def is_palindrome(string):
    if len(string) <= 1:
        return True
    return string[0] == string[-1] and is_palindrome(string[1:-1])


print(is_palindrome("stepik"))  # False
print(is_palindrome("level"))  # True
print(is_palindrome("abcca"))   # False
