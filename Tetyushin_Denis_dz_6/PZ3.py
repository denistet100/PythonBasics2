# 3. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
# Загрузить данные из обоих файлов и сформировать словарь: ключи — ФИО, значения — данные о хобби.
# Сохранить словарь в файл. Проверить сохранённые данные.
# Техническое задание
#
# Данные файлов синхронизированы построчно: 1-ой строке файла с ФИО соответствует 1-ая строка файла с хобби и т.п.
# При хранении данных используется принцип: одна строка — один пользователь.
# Разделитель между значениями — запятая. Не используем пакеты для парсинга CSV файлов.
# Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО,
# то для оставшихся ФИО использовать вместо хобби None.
# Если наоборот — формируем словарь, исходя из количества ФИО и выходим из скрипта с кодом «1».
# При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.
# Вы можете использовать здесь функции zip и zip_longest, но лучше обойтись без них.
# Примеры/Тесты:
#
# Фрагмент файла с данными о пользователях (task_3_users.csv):
#
#
# Иванов,Иван,Иванович
# Петров,Петр,Петрович
#
# Фрагмент файла с данными о хобби (task_3_hobby.csv):
#
#
# скалолазание,охота
# горные лыжи
#
# Фрагмент результирующего файла (task_3_rezult.txt):
#
#
# {'ИИИ': 'скалолазание,охота', 'ППП': 'горные лыжи'}


# rezult_dict = {}

def fio_def(line):
    surname, name, patronymic = line.strip().split(',')
    surname = surname.split()
    name = name.split()
    patronymic = patronymic.split()
    fio = (f"{surname[0][0]}{name[0][0]}{patronymic[0][0]}")
    return fio


def hobby_def(line_hobby):
    return line_hobby.strip()


with open("task_3_users.txt", encoding="UTF-8", mode="tr") as fio_file:
    fio_lines = fio_file.readlines()

with open("task_3_hobby.txt", encoding="UTF-8", mode="tr") as hobby_file:
    hobby_lines = hobby_file.readlines()

#
fio_hobby = {}
counter = 0
number_of_rows_fio = len(fio_lines)
number_of_rows_hobby = len(hobby_lines)

if number_of_rows_fio >= number_of_rows_hobby:
    longer_rows = number_of_rows_fio
else:
    longer_rows = number_of_rows_hobby

for counter in range(longer_rows):
    fio_letters = fio_def(fio_lines[counter])
    if counter < len(hobby_lines):
        fio_hobby[fio_letters] = hobby_def(hobby_lines[counter])
    elif number_of_rows_fio > number_of_rows_hobby:
        fio_hobby[fio_letters] = None
    else:
        exit(1)
print(fio_hobby)

with open("task_3_rezult.txt", encoding="UTF-8", mode="tw") as file_out:
    file_out.write(str(fio_hobby))
