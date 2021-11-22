# 4. Написать свой модуль utils и перенести в него функцию currency_rates и currency_rates_advanced,
# если вы решали задание 2.
# Создать скрипт, импортировать в него модуль utils и выполнить несколько вызовов функции currency_rates.
# Убедиться, что ничего лишнего не происходит.
# Техническое задание

# В модуле utils не должно быть ничего лишнего, только создание функций.
# Если вы считает нужным поместить туда дополнительную инфу, например тесты - используйте конструкцию main.
# Основной скрипт импортирует модуль или требуемые функции модуля, например currency_rates и currency_rates_advanced.
# После импорта выполните вызов функций, аналогичный заданию 1 (и 2), чтобы убедиться, что все импортировалось верно.
# Примечание:

# Обратите внимание, что название создаваемого модуля совпадает с названием импортируемого из requests.
# Это не вызовет конфликтов.

from utils import currency_rates, currency_rates_advanced       # , currency_rates_advanced

url_web = 'http://www.cbr.ru/scripts/XML_daily.asp'
# Тест
print('url_web = "http://www.cbr.ru/scripts/XML_daily.asp"', '\n',
      currency_rates(url_web, "USd"), '\n',
      currency_rates(url_web, "EuR"), '\n',
      currency_rates(url_web, "GBP"), '\n',
      currency_rates(url_web, "GBP2"), '\n')

# Тест
print('url_web = "http://www.cbr.ru/scripts/XML_daily.asp"', '\n',
       currency_rates_advanced(url_web, "USd"), '\n',
       currency_rates_advanced(url_web, "EuR"), '\n',
       currency_rates_advanced(url_web, "GBP"), '\n',
       currency_rates_advanced(url_web, "GBP2"), '\n')
