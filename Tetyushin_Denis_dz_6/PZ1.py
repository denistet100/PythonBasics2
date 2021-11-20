# 1. Распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
# Формат вывода результата:
#
#
# [
#     ...
#     ('141.138.90.60', 'GET', '/downloads/product_2'),
#     ('141.138.90.60', 'HEAD', '/downloads/product_2'),
#     ('173.255.199.22', 'GET', '/downloads/product_1'),
#     ...
# ]
#
# Техническое задание
#
# Не использовать библиотеки для парсинга. Только работа со строками.
# Создать список кортежей вида: `(<remote_addr>, <request_type>, <requested_resource>)`. Именно список кортежей.
# Код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.
# Вывести список на экран.
# Примечание:
#
# Файл логов можно загрузить отсюда:
# https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs
# Усложнение
#
# Уверены ли вы, что шаблон строк всегда одинаков?
# Попробуйте придумать как оценить идентичность шаблона строк файла.

list_in_file = []

with open("nginx_logs.txt", encoding="UTF-8", mode="tr") as my_file_new:
    for line in my_file_new:
        rm_adr, type_and_resource, *superfluous = line.split('"')
        rm_adr = rm_adr.split()
        type_and_resource = type_and_resource.split()
        remote_adr = rm_adr[0]
        request_type = type_and_resource[0]
        requested_resource = type_and_resource[1]
        list_in_file.append((remote_adr, request_type, requested_resource))


for el in list_in_file:
    print(el)
