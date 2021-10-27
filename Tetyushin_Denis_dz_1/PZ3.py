#3. Реализовать склонение слова «процент» для чисел до 234.
#Например, задаем число 5 — получаем «5 процентов», задаем число 2 — получаем «2 процента».
#Вывести все склонения для проверки.

number = int(input('Пользователь, введите целое положительне число n: '))
def draw(number_a):
    end_number = number_a % 10
    if (end_number == 0 or (end_number > 4 and end_number < 10) or (number_a > 4 and number_a < 21)):
        print(number_a, 'процентов')
    elif (end_number == 1):
        print(number_a, 'процент')
    elif (end_number > 1 and end_number < 5):
        print(number_a, 'процента')

draw(number)

for i in range(0, 21, +1):
    draw(i)
