# 5. [Задача со звездочкой]: Доработать скрипт из предыдущего задания: теперь он должен работать и из консоли.
# Используйте аргументы командной строки.
# Техническое задание
#
# Скрипт должен корректно обрабатывать только одну переданную ему валюту.
# Сделайте значимые сообщения пользователю о работе скрипта
# Скрипт могут запустить вообще без параметров, а могут с любым количеством параметров. Это надо учесть.
# Сделайте скриншот нескольких вызовов скрипта с разными аргументами.
# Примеры/Тесты:
#
#
# py task-4_5.py USD
#        USD: 71.7846
# py task-4_5.py FFF
#        FFF: Не найдена валюта
#
# Алгоритм
#
# Если вы хотите использовать распаковку, подумайте не будет ли ошибок.

# так нам нужен argv
# если пустое значение то вывод отсутствует а длинна = 1

from sys import argv
from utils import currency_rates, currency_rates_advanced

url_web = 'http://www.cbr.ru/scripts/XML_daily.asp'

if len(argv) > 1:            # Скрипт должен корректно обрабатывать только одну переданную ему валюту.
    currency_input = argv[1]
    print(f"{argv[0]}:   {currency_rates(url_web, currency_input)}")
    print(f"{argv[0]}:   {currency_rates_advanced(url_web, currency_input)}")
else:
    print('Error name currency')