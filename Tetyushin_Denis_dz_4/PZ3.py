# 3. [Задача со звездочкой]: усложненный вариант задания 2.
# Доработать функцию currency_rates: теперь она должна возвращать курс валюты и дату,
# которая передаётся в ответе сервера. Название новой функции currency_rates_advanced.
# Формат вывода результата:
#
# Вызовите функцию для нескольких валют, обязательно для несуществующей валюты.
# Техническое задание
#
# Все требования задания 2 остаются в силе.
# Функция должна вернуть список или кортеж, содержащий дату и курс валюты.
# Дата должна быть объектом date пакета datetime стандартной библиотеки.
# Для ее создания используйте функции пакета datetime. Если это слишком сложно - оставьте дату строкой.
# Примеры/Тесты:
#
#
# >>> url = "<http://www.cbr.ru/scripts/XML_daily.asp>"
# >>> currency_rates_advanced(url, "USd")
# ([datetime.date(2021, 10, 15)], 71.7846)
# >>> currency_rates_advanced(url, "EuR")
# ([datetime.date(2021, 10, 15)], 83.3347)
# >>> currency_rates_advanced(url, "GBP")
# ([datetime.date(2021, 10, 15)], 98.3449)
# >>> currency_rates_advanced(url, "GBP2")
# ([datetime.date(2021, 10, 15)], None)
#
# Алгоритм
#
# Посмотрите ответ сервера, как с минимальными усилиями вытащить оттуда дату?
# Подумайте можно ли, и правильно ли вызывать из этой функции функцию предыдущей задачи: currency_rates
# Если есть требования, что мы используем обе функции в своей работе, как соблюсти принцип DRY?

from requests import get, utils
import decimal
from datetime import date

def currency_rates_advanced(url, currency):

    currency = currency.upper()

    response = get(url)
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)  # Информация с сайта

    currency_index = content.find(currency)  # нашли индекс названия валюты в контексте, если не существует = -1

    if currency_index != -1:
        res_list = []
        prise_cur_fl = float(content[content.find("<Value>", currency_index) + len("<Value>"):
                                     content.find("</Value>", currency_index)].replace(",", "."))
        prise_cur_dc = decimal.Decimal(prise_cur_fl).quantize(decimal.Decimal('.001'))
        #cur_data = datetime.fromtimestamp(content[content.find('<ValCurs Date="', 1) + len('<ValCurs Date="'):
        # content.find('" name=', 1)].replace(".", ","))
        cur_data_srt = (content[content.find('<ValCurs Date="', 1) + len('<ValCurs Date="'): content.find('" name=', 1)])
        cur_data_day = cur_data_srt[0:2]
        cur_data_month = cur_data_srt[3:5]
        cur_data_year = cur_data_srt[6:]
        cur_data = date.fromisoformat(f"{cur_data_year}-{cur_data_month}-{cur_data_day}")
        #print(cur_data_day)
        #print(cur_data_month)
        #print(cur_data_year)
        res_list.append(cur_data)
        res_list.append(prise_cur_dc)
        #print(res_list)
        return res_list
    else:
        error = 'Error name currency'
        return error


url_web = 'http://www.cbr.ru/scripts/XML_daily.asp'

# Тест
print('url_web = "http://www.cbr.ru/scripts/XML_daily.asp"', '\n',
       currency_rates_advanced(url_web, "USd"), '\n',
       currency_rates_advanced(url_web, "EuR"), '\n',
       currency_rates_advanced(url_web, "GBP"), '\n',
       currency_rates_advanced(url_web, "GBP2"), '\n')

currency_input = input('Введите валюту: ')
#currency_input = "usd"
print(currency_rates_advanced(url_web, currency_input))
