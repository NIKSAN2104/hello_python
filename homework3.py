# №1 Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной идексах.

# def in_list(my_list):
#     s = 0
#     for i in range(len(my_list)):
#         if i % 2 != 0:
#             s += my_list[i]
#     print(f"Сумма равна: {s}")

# my_list = [2, 3, 5, 9, 3]
# in_list(my_list)



# №2 Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# def in_list(my_list):
#     l = len(my_list) // 2 + 1 if len(my_list) % 2 != 0 else len(my_list) // 2

#     new_lst = [my_list[i] * my_list[len(my_list) - i - 1] for i in range(l)]
#     print(new_lst)

# my_list = list(map(int, input("Введите числа через пробел:\n").split()))
# in_list(my_list)



# №3 Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# my_list = list(map(float, input("Введите числа через пробел:\n").split()))
# new_list = [round(i%1,2) for i in my_list if i%1 != 0]
# print(max(new_list) - min(new_list))



# №4 Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# dec = ""
# n = int(input("Введите число для преобразовывания десятичного числа в двоичное:\n"))
# while n != 0:
#     dec = str(n%2) + dec
#     n //=2
# print(dec)



# №5 Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:- для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

# while True:
#     try:
#         num: int = int(input('Введите число: '))
#         break
#     except ValueError:
#         print(f'Это не число.')


# def decorator(func):

#     def wrapper(*args):
#         print(f'Начало решения!\n{"-"*60}')
#         func(*args)
#         print(f'{"-"*60}\nОкончание решения!')

#     return wrapper


# @decorator
# def prints_text(func1: list[int], func2: list[int]):
#     print(f'Негафибоначчи & Фибоначчи:\n{func2 + func1[1:]}')


# def fibonacci(number: int):
#     inner_list: list[int] = []
#     for item in range(number+1):
#         match item:
#             case 0 | 1:
#                 inner_list.append(item)
#             case _:
#                 inner_list.append(inner_list[item-2]+inner_list[item-1])
#     return inner_list


# def negafibonacci(number: int):
#     inner_list: list[int] = []
#     for item in range(number + 1):
#         match item:
#             case 0 | 1:
#                 inner_list.insert(0, item)
#             case _:
#                 inner_list.insert(0, (inner_list[1] - inner_list[0]))
#     return inner_list


# prints_text(fibonacci(num), negafibonacci(num))