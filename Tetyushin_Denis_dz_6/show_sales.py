# 4. Реализовать простую систему хранения данных о суммах продаж булочной.
# Должно быть два скрипта с интерфейсом командной строки: для записи данных и для вывода на экран записанных данных.
# Техническое задание
#
# Данные хранить в файле bakery.csv в кодировке utf-8.
# Соблюдаем формат данных в файле: одна запись (цифра) это одна строка.
# При записи передавать из командной строки значение суммы продаж. Функцию input не использовать.
# Новая запись дозаписывается в конец файла. Имя исполняемого скрипта: add_sale.py
# Для чтения данных реализовать в командной строке следующую логику. Предполагаем, что первая запись имеет номер 1.
# просто запуск скрипта — выводить все записи;
# запуск скрипта с одним параметром-числом — выводить все записи от номера, равного этому числу, до конца;
# запуск скрипта с двумя числами — выводить записи, начиная от номера, равного первому числу,
# по номер, равный второму числу, включительно;
# Корректно обработать неправильное количество или тип переданных параметров.
# Имя исполняемого скрипта: show_sales.py
# Примеры/Тесты:
# Примеры запуска скриптов:
#
#
# python add_sale.py 5978
# python add_sale.py 891
# python add_sale.py 7879
# python add_sale.py 1573
# python show_sales.py
# 5978
# 891
# 7879
# 1573
# python show_sales.py 3
# 7879
# 1573
# python show_sales.py 1 3
# 5978
# 891
# 7879
#
# Алгоритм
#
# Для удобства отладки кода - разделите его на два этапа:
# отдельно отладьте алгоритм получения данных из командной строки:
# получение и обработка; и отдельно отлаживайте алгоритм работы с записями файла.
# На втором этапе «переданные параметры» можно сразу внести в код и не работать с командной строкой.
# Усложнение Подумать, как избежать чтения всего файла в память при реализации второго и
# третьего случаев чтения данных.

from sys import argv

len_enter = len(argv)

with open("bakery.csv", encoding="UTF-8", mode="rt") as my_file:
    if len_enter == 1:
        for line in my_file:
            print(line.strip())
    elif len_enter == 2:
        for el, line in enumerate(my_file):
            if el >= int(argv[1]):
                print(line.strip())
    elif len_enter == 3:
        for el, line in enumerate(my_file):
            if int(argv[1]) - 1 <= el <= int(argv[2]):
                print(line.strip())
    else:
        print("Input error")
