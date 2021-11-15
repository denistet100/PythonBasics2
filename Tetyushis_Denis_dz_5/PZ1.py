# 1. Написать генератор нечётных чисел от 1 до n (включительно), без использования ключевого слова yield,
# полностью истощить генератор.
# Формат вывода результата:
#
# Программа явно должна закончиться на StopIteration
# Техническое задание
#
# n - любое положительное число.
# Не путайте истощение итератора и печать его значений. Явно дойдите до StopIteration.
# Истощение генератора - любым удобным для вас способом. Например создаем генератор в программе,
# а истощаем руками в консоли.
# Создание генератора сделайте внутри функции iterator_without_yield(n),
# примающей аргументом n любое положительное число и возвращающей генератор.
# Примеры/Тесты:
#
#
# gen1 = iterator_without_yield(11)
# next(gen1)
# 1
# next(gen1)
# 3
# next(gen1)
# 5
# next(gen1)
# 7
# next(gen1)
# 9
# next(gen1)
# 11
# next(gen1)
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# StopIteration
#
# Усложнение [одна звездочка]:
# нужен генератор нечётных чисел от 1 до n (включительно), для чисел, квадрат которых меньше 200.
# Все остальное как в основном задании.


def iterator_without_yield(n):
    gen = (el for el in range(1, n + 1, 2))
    return gen


def iterator_without_yield_square(n):
    gen = (el for el in range(1, n + 1, 2) if el**2 < 200)
    return gen


# nmbr = int(input('nmbr = '))

nmbr = 10

gen1 = iterator_without_yield(nmbr)

for i in gen1:
    print(i)

while True:
    print(gen1)
    break
