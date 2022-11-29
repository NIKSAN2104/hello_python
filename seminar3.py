# Задание №2

my_list = ['sdf13', 'fds66', '34']

def in_list(list_, find_):
    result = False
    for i in list_:
        if find_ in i:
            result = True
            print(i)
    return result

print(in_list(my_list, '3'))


# Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что ее нет.

def fun():
    list = ['qwe', 'asd', 'zxc', 'qwe', 'ertqwe']
    a = input('Введите число: ')
    count = 0
    for i in range(len(list)):
        if list[i] == a:
            count += 1
            if count == 2:
                return i
    return -1

print(fun())