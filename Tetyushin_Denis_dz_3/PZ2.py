#2. [Задача со звездочкой]: усложненный вариант задания 1.
#Написать функцию num_translate_adv, которая корректно обработает числительные, начинающиеся с заглавной буквы.
#Если перевод сделать невозможно, вернуть объект None.

dictionary = { "zero":"нуль", "one":"один", "two":"два", "three":"три", "four":"четыре", "five":"пять", "six":"шесть", "seven":"семь", "eight":"девять", "nine":"девять", "ten":"десять", }
dictionary_big = { "Zero":"Нуль", "One":"Один", "Two":"Два", "Three":"Три", "Four":"Четыре", "Five":"Пять", "Six":"Шесть", "Seven":"Семь", "Eight":"Девять", "Nine":"Девять", "Ten":"Десять", }


def num_translate(wrd):
    
    if (dictionary.get(wrd) != None):
        print('перевод: ', dictionary.get(wrd))
    else:
        print('перевод: ', dictionary_big.get(wrd))

word = input('Введите число по англ от 1 до 10: ')

num_translate(word)
