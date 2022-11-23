# №1. Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.

day = int(input('Введите день недели от 1 до 7: '))
if 0 < day < 6:
   print('Этот день не является выходным')
else:
    5 < day < 8
    print('Этот день является выходным')


# №2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат. 
# ⋀ - and ⋁ - or ¬ - not

print('Проверка истинности утверждения: ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.')
for i in range (2):
    x = False
    if i == 1:
        x = True
    for j in range (2):
        y = False
        if j == 1:
            y = True
        for l in range (2):
            z = False
            if l == 1:
                z = True
            print(f'X = {x}, Y = {y}, Z = {z}, answer = {not(x or y or z) == (not x and not y and not z)}')


# №3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер 
# четверти плоскости, в которой находится эта точка.

x = int(input('Введите координату x: '))
y = int(input('Введите координату y: '))

if x != 0 and y != 0:
    if x > 0:
        if y > 0:
            print('Первая четверть')
        else:
            print('Четвертая четверть')
    else:
        if y > 0:
            print('Вторая четверть')
        else:
            print('Третья четверть')


# №4. Напишите программу, которая по заданному номеру четверти, показывает 
# диапазон возможных координат точек в этой четверти (x и y).

quarter = int(input('Введите номер четверти: '))
if quarter == 1:
    print('x = (0, +бесконечность), y = (0, +бесконечность)')
elif quarter == 2:
    print('x = (-бесконечность, 0), y = (0, +бесконечность)')
elif quarter == 3:
    print('x = (-бесконечность, 0), y = (-бесконечность, 0)')
elif quarter == 4:
    print('x = (0, +бесконечность), y = (-бесконечность, 0)')
else:
    print('Введите правильный номер')


# Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.


x1 = int(input('Введите координаты x1:'))
y1 = int(input('Введите координаты y1:'))
x2 = int(input('Введите координаты x2:'))
y2 = int(input('Введите координаты y2:'))

import math
distance = math.sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))
print(f'расстояние = {round(distance, 3)}')