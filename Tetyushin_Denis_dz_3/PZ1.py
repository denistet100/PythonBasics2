#1. Написать функцию num_translate, переводящую числительные от 0 до 10 c английского на русский язык.
#Если перевод сделать невозможно, вернуть объект None.

dictionary = { "zero":"нуль", "one":"один", "two":"два", "three":"три", "four":"четыре", "five":"пять", "six":"шесть", "seven":"семь", "eight":"девять", "nine":"девять", "ten":"десять"}

def num_translate(wrd):
    print('перевод: ', dictionary.get(wrd))

word = input('Введите число по англ от 1 до 10: ')

num_translate(word)
