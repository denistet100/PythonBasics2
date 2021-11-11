#5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов,
#взятых из трёх заданных списков:

from random import choice
import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def get_jokes(n):
    jokes = []

    for i in range(n):
        random_index1 = random.choice(nouns)
        random_index2 = random.choice(adverbs)
        random_index3 = random.choice(adjectives)
        string = (random_index1 + ' ' + random_index2 + ' ' + random_index3)
        print(string)
        jokes.append(string)
        print(jokes)

    
nmbr = int(input('Введи число:'))

get_jokes(nmbr)
