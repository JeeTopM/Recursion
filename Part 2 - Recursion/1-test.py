'''
Вам доступна функция traffic(), реализованная с помощью цикла while, 
которая принимает в качестве аргумента число n и выводит n раз строку Не парковаться.
Перепишите данную функцию с использованием рекурсии, чтобы она выполняла ту же задачу.
'''

'''
# Старое
def traffic(n):
    while n > 0:
        print('Не парковаться')
        n -= 1
traffic(2)
'''

def traffic(n):
    if n > 0:
        print('Не парковаться')
        traffic(n - 1)

traffic(2)