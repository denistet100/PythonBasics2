#6. [Задача со звездочкой]: усложненный вариант задания 5.
#Добавьте в функцию еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках: каждое слово можно использовать только в одной шутке.
#Техническое задание
#1.	Проверьте работу функции для разного количества шуток. Убедитесь в том, что каждое слово встречается только один раз.
#Примечание:
#1.	Внимательно посмотрите какие из функций модуля random, упомянутые в методичке, подходят для реализации уникальности.
#2.	Подумайте о том, сколько шуток можно вернуть при требовании уникальности, как это связано с размерами списков.

from random import choice
import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def get_jokes(n, fl):
    jokes = []

    for i in range(n):
        random_index1 = random.choice(nouns)
        random_index2 = random.choice(adverbs)
        random_index3 = random.choice(adjectives)
        if fl == True:
            nouns.remove(random_index1)
            adverbs.remove(random_index2)
            adjectives.remove(random_index3)
        string = (random_index1 + ' ' + random_index2 + ' ' + random_index3)
        print(string)
        jokes.append(string)
        print(jokes)

nmbr = int(input('Введи число:'))
if (nmbr < len(nouns) and nmbr < len(adverbs) and nmbr < len(adjectives)):
    flag = bool(input('Введи что хочешь если не надо повторять слова:'))
else:
    flag = False
get_jokes(nmbr, flag)
