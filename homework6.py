# №1. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
# while True:
#     try:
#         entered_list: list[int] = list(map(int, input('Введите числа через пробел: ').split()))
#         break
#     except ValueError:
#         print(f'Это не число.')


# def decorator(func):

#     def wrapper(*args):
#         print(f'Начало решения!\n{"-"*45}')
#         func(*args)
#         print(f'{"-"*45}\nОкончание решения!')

#     return wrapper


# def product_of_pairs_of_numbers(search_list: list[int]) -> list[int]:
#     arg_list: list[int] = [search_list[item]*search_list[-(1+item)] for item in range(int(len(search_list)+1)//2)]
#     return arg_list


# @decorator
# def prints_text(inner_list: list[int], func: list[int]):
#     print(f'Исходный список: {inner_list}\nИтоговый список: {func}')


# prints_text(entered_list, product_of_pairs_of_numbers(entered_list))











# №2. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся
# элементов исходной последовательности.
# Ввод: [1, 1, 2, 3, 4, 4, 4]
# Вывод: [2, 3]

# from collections import Counter


# def value_input() -> list[int]:
#     while True:
#         try:
#             value: list[int] = list(map(int, (input('Введите последовательность чисел через пробел: ').split())))
#             return value
#         except ValueError:
#             print(f'Это не число.')


# def decorator(func):

#     def wrapper(*args):
#         print(f'Начало решения!\n{"-"*45}')
#         func(*args)
#         print(f'{"-"*45}\nОкончание решения!')
#     return wrapper


# @decorator
# def text_printing(inner_list: list[int]):
#     print(f'Список неповторяющихся элементов исходной последовательности: {inner_list}')


# def search_for_non_repeating_elements(inner_list: list[int]) -> list[int]:
#     number_of_identical_elements: dict[int, int] = Counter(inner_list)
#     elements_that_occur_once: list[int] = [key for key, value in number_of_identical_elements.items() if value == 1]
#     return elements_that_occur_once


# text_printing(search_for_non_repeating_elements(value_input()))












# №3. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных индексах. Индексы вводятся одной строкой, через пробел.
# n = 3
# [-3, -2, -1, 0, 1, 2, 3]
# --> 0 2 3
# -3 * -1 * 0 = 0
# Вывод: 0
# from functools import reduce


# def get_number() -> list[int]:
#     while True:
#         entered_number: str = input('Введите целое положительное число: ')
#         if entered_number.isdigit():
#             return [i for i in range(-int(entered_number), int(entered_number)+1)]
#         print('Ошибка! Вы ввели не число!')


# def get_index():
#     while True:
#         list_iterable: list[int] = get_number()
#         index_list: list[int] = list(map(int, input('Введите индексы одной строкой, через пробел: ').split()))
#         if len(list_iterable)-1 >= max(index_list):
#             return list_iterable, index_list
#         print('Ошибка! Вы ввели не верный индекс!')


# def get_index_multiplication():
#     list_iterable, index_list = get_index()
#     value = reduce(lambda x, y: x * y, [list_iterable[i] for i in range(len(list_iterable)) if i in index_list])
#     return index_list, list_iterable, value


# finish_list = get_index_multiplication()
# print(f'\nПроизведение индексов {finish_list[0]} в списке {finish_list[1]}\nВывод: {finish_list[2]}')