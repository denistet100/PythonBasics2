# 2. Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, …)
# и возвращающую курс этой валюты по отношению к рублю.
# Формат вывода результата:
#
# Вызовите функцию для нескольких валют, обязательно для несуществующей валюты.
# Техническое задание
#
# Использовать библиотеку requests. В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp.
# Выполнить предварительно запрос к API в обычном браузере, посмотреть содержимое ответа.
# В каком формате возвращен ответ?
# Функция принимает два аргумента: строка с URL, куда стучимся и строку с кодом валюты (только одной).
# Возвращает результат числового типа, например float. Если в качестве аргумента передали код валюты,
# которого нет в ответе, вернуть объект None.
# Для извлечения данных использовать только методы объект str.
# Сделать работу функции не зависящей от того, в каком регистре был передан аргумент.
# Функция должна корректно обрабатывать любой код валюты. Правильность параметра url можно не проверять.
# Вводить коды валют с клавиатуры (input) необязательно.
# Примеры/Тесты:
#
#
# >>> url = "<http://www.cbr.ru/scripts/XML_daily.asp>"
# >>> currency_rates(url, "USd")
# 71.7846
# >>> currency_rates(url, "EuR")
# 83.3347
# >>> currency_rates(url, "GBP")
# 98.3449
# >>> currency_rates(url, "GBP2")
# >>>
#
# Алгоритм
#
# Пример использования requests есть в методичке.
# Внимательно посмотрите все методы объекта str, которыми вы можете пользоваться. Обратите внимание,
# что у методов могу быть параметры, которые сильно облегчат вам работу.
# Помните, срез строки создает копию. Уверены ли вы, что вам нужна копия именно такого размера?
# Это увеличивает время выполнения и расходует память. Аналогично функция поиска требует времени для работы,
# можно ли оптимизировать поиск?
# Подумайте: есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal?
# Сильно ли усложняется код функции при этом?
# Вспомните в каких случаях функция возвращает None.

from requests import get, utils
import decimal

# Написать функцию currency_rates(url, currency)

# преобразовать в заглавные?
# str.upper()

# код для изъятия информации с сайта
# response = get(url)
# encodings = utils.get_encoding_from_headers(response.headers)

# сам контент с сайта - пока найдёшь повесишься
# content = response.content.decode(encoding=encodings)
# как найти валюту?             создать словарь как на уроке?          через if?
# как далеко она стоит?


# отсеить ввод ошибок        вывод ошибки
# перебрать все символы от и до и собрать
# добавить символ и получить число?     с помощью контекста востановить? откуда до куда? <Value> </Value>
# получить с плавающей точкой                   КАК!!!????
# получить с денежный

def currency_rates(url, currency):

    currency = currency.upper()
    # print(currency)

    response = get(url)
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)  # Информация с сайта

    # print(response)
    # print(encodings)
    # print(content)
    # print(currency_index)

    currency_index = content.find(currency)  # нашли индекс названия валюты в контексте, если не существует = -1

    if currency_index != -1:
        # for ch_index in range(content.find("<Value>", currency_index) + len("<Value>"),
        # content.find("</Value>", currency_index), 1):
        # prise_cur = decimal.Decimal(content[content.find( "<Value>", currency_index) + len("<Value>"):
        # content.find("</Value>", currency_index)])
        # Сразу вывели цену валюты в типе для денег, из контекста по индексам от валюты до валюты\

        prise_cur_fl = float(content[content.find("<Value>", currency_index) + len("<Value>"):
                                     content.find("</Value>", currency_index)].replace(",", "."))
        # Я не навижу эту запятую! Часа два не мог понять что не так! А ТАМ ТОЧКА ДОЛЖНА БЫТЬ!!!!

        prise_cur_dc = decimal.Decimal(prise_cur_fl).quantize(decimal.Decimal('.001'))
        return prise_cur_dc
    else:
        error = 'Error name currency'
        return error


url_web = 'http://www.cbr.ru/scripts/XML_daily.asp'

# Тест
print('url_web = "http://www.cbr.ru/scripts/XML_daily.asp"', '\n', currency_rates(url_web, "USd"), '\n', currency_rates(url_web, "EuR"), '\n', currency_rates(url_web, "GBP"), '\n', currency_rates(url_web, "GBP2"), '\n')

currency_input = input('Введите валюту: ')
# currency_input = "usd"
print(f"{currency_rates(url_web, currency_input)}")
