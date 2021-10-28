#2. Для кубов нечётных чисел от 1 до 1000.
#Вычислить сумму чисел, сумма цифр кубов которых делится нацело на 7.

while True:
    summ = 0
    for i in range(1, 1001, +2):
        A = True
        summc = 0
        buf = i ** 3
        while (A == True):
            summc = summc + buf % 10
            buf//=10
            if (buf==0):
                A = False
        if (summc % 7 == 0):
            summ = summ + i
    print(summ)
    break
