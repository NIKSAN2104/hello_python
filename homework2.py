# №1 Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

num = float(input('Введите вещественное число: '))
i = 0
sum = 0
for i in str(num):
    if i != '.':
        sum += int(i)
print(f'Сумма цифр заданного числа --> {sum}')



# №2 Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

num = int(input('Введите число N: '))

def mult(n):
    if n == 1:
        return 1
    else:
        return n * mult(n - 1)

list = []
for i in range(1, num + 1):
    list.append(mult(i))

print(f"Произведения чисел от 1 до {num}:  {list}")



# №3 Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.
# Пример:
# Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44} Сумма 9.06

num = input('Введите целое положительное число: ')

list_number = [round((1 + 1/i)**i, 2) for i in range(1, int(num) + 1)]
print(sum(list_number))



# №4 Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных индексах. Индексы вводятся одной строкой, через пробел.

def get_index(num):
    while True:
        entered_index_list = input('Введите ндексы одной строкой, через пробел: ').split()
        index_list = list(map(int, entered_index_list))
        if num*num+1 > max(index_list):
            return index_list
        print('Ошибка! Вы ввели не верный индекс!')


def get_index_multiplication(num, index_list):
    new_list = [i for i in range(-num, num+1)]
    value = 1
    for item in index_list:
        value *= new_list[item]
    return new_list, value


num = int(input('Введите целое положительное число: '))
index_list = get_index(num)
new_list, multiplication = get_index_multiplication(num, index_list)
print(f'\nПроизведение индексов {index_list} в списке {new_list}\nВывод: {multiplication}')


# №5 Реализуйте алгоритм перемешивания списка.

from random import shuffle

entered_list = input('Введите элементы списка одной строкой, через пробел: ').split()
shuffle(entered_list)
print(entered_list)