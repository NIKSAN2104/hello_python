# №1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

#string = 'привет, приабввет, это эабвтТо мое абвмое Д дабвомОабвашнее абвзадаЖЖнабвие З'

#print(*[i for i in string.split() if not'абв' in i])


# №2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
# from random import randint

# candies: int = 2021


# def game_selection(cand) -> str:
#     while True:
#         try:
#             players: int = int(input(f"Игра с компьютером ----> 1\n"
#                                      "Игра с другом ---------> 2\n"
#                                      "Введите 1 или 2--------> "))
#             if players == 1 or players == 2:
#                 print(f'На столе лежит {cand} конфета, каждый игрок берёт от 1 до 28 конфет.\n'
#                       f'Забирает все конфеты тот кто сделает последний ход!\n')
#                 return "pve" if players == 1 else "pvp"
#             else:
#                 print("Для игры нужно выбрать!!!")
#         except ValueError:
#             print("Нужны цифры 1 или 2!!!")


# def lottery(name) -> int:
#     one = 'Player 1'
#     two = 'Player 2'
#     if name == 'pve':
#         two = 'Компьютер'
#     print(f'Жеребьевка.')
#     pl_one = randint(1, 10)
#     print(f'{one} выбросил {pl_one}')
#     pl_two = randint(1, 10)
#     print(f'{two} выбросил {pl_two}')
#     return 1 if pl_one > pl_two else 2


# def moves(cand: int, player: int, game: str) -> tuple[int, int]:
#     if game == "pvp":
#         cand -= number_entry(cand)
#     else:
#         if player == 1:
#             cand -= number_entry(cand)
#         else:
#             cand -= virtual_player(cand)
#     print(f'Всего осталось {cand} конфет.')
#     player = 2 if player == 1 else 1
#     return cand, player


# def number_entry(cand: int) -> int:
#     while True:
#         try:
#             num: int = int(input(f'Введите число от 1 до {28 if cand > 28 else cand} --> '))
#             if num <= cand:
#                 if 0 < num < 29:
#                     break
#                 else:
#                     print('Число не подходит!')
#             else:
#                 print(f'Конфет осталось {cand}!')
#         except ValueError:
#             print('Вы ввели не число!')
#     return num


# def virtual_player(cand: int) -> int:
#     max_number: int = 28
#     if cand <= max_number:
#         num = cand
#     elif cand % 28 == 0:
#         num = 28 - 1
#     elif cand % 28 == 1:
#         if (cand // 28) % 2 == 1:
#             num = 28 - 1
#         else:
#             num = 28
#     else:
#         num = cand % 28 - 1
#     print(f'Он взял {num}!')
#     return num


# def candy_game(game: str, cand: int) -> int:
#     player: int = lottery(game)
#     if game == "pve" and player == 2:
#         print(f'Первым начинает Compi\n')
#     else:
#         print(f'Первым начинает Player {player}\n')
#     while True:
#         if cand > 0:
#             if game == "pve" and player == 2:
#                 print('Ходит компьютер!')
#                 cand, player = moves(cand, player, game)
#             else:
#                 print(f'Ходит Player {player}')
#                 cand, player = moves(cand, player, game)
#         else:
#             player = 2 if player == 1 else 1
#             print(f'Игра закончилась: '
#                   f'{"победил Компьютер" if game == "pve" and player == 2 else f"победил игрок {player}"}!')
#             return player


# candy_game(game_selection(candies), candies)


# №2.1. 
# import tkinter as tk
# from tkinter import messagebox as mesg
# from random import randint


# def add_digit(digit):
#     candys = candy_counter.get()
#     value = player_field.get()
#     if int(candys) < int(digit) and value == 'от 1 до 28':
#         mesg.showinfo('Внимание', f'Конфет осталось {candys}')
#     elif value != 'от 1 до 28' and int(candys) < int(value + digit):
#         mesg.showinfo('Внимание', f'Конфет осталось {candys}')
#     elif value == 'от 1 до 28':
#         value = str(digit)
#     elif value == '0':
#         value = str(digit)
#     elif len(value) < 2:
#         value += str(digit)
#         if int(value) > 28:
#             mesg.showinfo('Внимание', 'Будет больше 28 конфет')
#             value = value[0]
#     else:
#         mesg.showinfo('Внимание', 'Будет больше 28 конфет')
#     player_field['state'] = tk.NORMAL
#     player_field.delete(0, tk.END)
#     player_field.insert(0, value)
#     player_field['state'] = tk.DISABLED


# def add_clear():
#     value = player_field.get()
#     player_field['state'] = tk.NORMAL
#     player_field.delete(0, tk.END)
#     player_field.insert(0, 'от 1 до 28')
#     player_field['state'] = tk.DISABLED


# def computer_walks():
#     candys = candy_counter.get()
#     if candys == '0':
#         mesg.showinfo('Ванилопа-Фон-Кекс', f'Неееет...\nЗабирай конфеты, ты победил.')
#         root.destroy()
#     else:
#         value = randint(1, 28) if int(candys) > 28 else candys
#         candy_counter['state'] = tk.NORMAL
#         candy_counter.delete(0, tk.END)
#         candys = int(candys) - int(value)
#         candy_counter.insert(0, candys)
#         candy_counter['state'] = tk.DISABLED
#         mesg.showinfo('Ванилопа-Фон-Кекс', f'Я взяла из кучи {value} конфет')
#         if candys == 0:
#             mesg.showinfo('Ванилопа-Фон-Кекс', f'Хи-хи-хи я победила.\nВсе конфеты мои!!!')
#             root.destroy()


# def add_operation():
#     value = player_field.get()
#     candys = candy_counter.get()
#     try:
#         candys = int(candys) - int(value)
#         player_field['state'] = tk.NORMAL
#         candy_counter['state'] = tk.NORMAL
#         player_field.delete(0, tk.END)
#         candy_counter.delete(0, tk.END)
#         candy_counter.insert(0, candys)
#         player_field.insert(0, 'от 1 до 28')
#         player_field['state'] = tk.DISABLED
#         candy_counter['state'] = tk.DISABLED
#         computer_walks()
#     except (ValueError, SyntaxError):
#         mesg.showinfo('Внимание', 'Нужны только цифры')
#         player_field['state'] = tk.NORMAL
#         player_field.delete(0, tk.END)
#         player_field.insert(0, 'от 1 до 28')
#         player_field['state'] = tk.DISABLED


# def make_digit_buttom(digit):
#     return tk.Button(text=digit, bd=5, bg="#22D822", font=("Arial bold", 12), command=lambda: add_digit(digit))


# def press_key(event):
#     print(repr(event.char))
#     if event.char.isdigit():
#         add_digit(event.char)
#     elif event.char == '\r':
#         add_operation()


# root = tk.Tk()
# root.title("Игра конфетки")
# root.geometry('300x250+450+150')
# root['bg'] = '#FA8072'
# root.resizable(False, False)
# root.bind('<Key>', press_key)

# candys = tk.Label(root, text="Конфеты", bg="#832EF2", fg='#8AED63', font=("Arial 14 bold"))
# candys.grid(column=0, row=0, columnspan=2, stick='wens', padx=5)
# candy_counter = tk.Entry(root, justify=tk.CENTER, bg="#C942F2", fg='#8AED63', font=("Arial 18 bold"), width=1)
# candy_counter.insert(0, "285")
# candy_counter['state'] = tk.DISABLED
# candy_counter.grid(column=0, row=1, columnspan=2, stick='wens', padx=4, pady=4)

# player = tk.Label(root, text="Возьми конфеты", bg="#832EF2", fg='#8AED63', font=("Arial 12 bold"))
# player.grid(column=2, row=0, columnspan=3, stick='wens', padx=5)
# player_field = tk.Entry(root, justify=tk.RIGHT, bg="#22D8D5", font=("Arial 14 bold"), width=1)
# player_field.insert(0, 'от 1 до 28')
# player_field['state'] = tk.DISABLED
# player_field.grid(column=2, row=1, columnspan=3, stick='wens', padx=4, pady=4)

# make_digit_buttom('1').grid(row=2, column=0, stick='wens', padx=5, pady=5)
# make_digit_buttom('2').grid(row=2, column=1, stick='wens', padx=5, pady=5)
# make_digit_buttom('3').grid(row=2, column=2, stick='wens', padx=5, pady=5)
# make_digit_buttom('4').grid(row=2, column=3, stick='wens', padx=5, pady=5)
# make_digit_buttom('5').grid(row=2, column=4, stick='wens', padx=5, pady=5)
# make_digit_buttom('6').grid(row=3, column=0, stick='wens', padx=5, pady=5)
# make_digit_buttom('7').grid(row=3, column=1, stick='wens', padx=5, pady=5)
# make_digit_buttom('8').grid(row=3, column=2, stick='wens', padx=5, pady=5)
# make_digit_buttom('9').grid(row=3, column=3, stick='wens', padx=5, pady=5)
# make_digit_buttom('0').grid(row=3, column=4, stick='wens', padx=5, pady=5)
# tk.Button(text='Взять', bd=5, bg="#F53D0A", font=("Arial Bold", 12), command=add_operation)\
#     .grid(row=4, column=0, columnspan=3, stick='wens', padx=5, pady=5)
# tk.Button(text='Удалить', bd=5, bg="#F5E90A", font=("Arial Bold", 12), command=add_clear)\
#     .grid(row=4, column=3, columnspan=2, stick='wens', padx=5, pady=5)

# root.grid_columnconfigure(0, minsize=60)
# root.grid_columnconfigure(1, minsize=60)
# root.grid_columnconfigure(2, minsize=60)
# root.grid_columnconfigure(3, minsize=60)
# root.grid_columnconfigure(4, minsize=60)

# root.grid_rowconfigure(2, minsize=60)
# root.grid_rowconfigure(3, minsize=60)
# root.grid_rowconfigure(4, minsize=60)

# mesg.showinfo('Правила игры', f'На столе лежат конфеты, каждый игрок берёт от 1 до 28 конфет.'
#                               f'\nКто делает последний ход - побеждает.\n\n'
#                               f'Победитель забирает все конфеты !')

# root.mainloop()


# №3. Создайте программу для игры в ""Крестики-нолики"".
# import pygame
# import sys


# def check_win(mas, sign):
#     zeroes = 0
#     for row in mas:
#         zeroes += row.count(0)
#         if row.count(sign) == 3:
#             return 'Победил X' if sign == 'x' else 'Победил O'
#     for col in range(3):
#         if mas[0][col] == sign and mas[1][col] == sign and mas[2][col] == sign:
#             return 'Победил X' if sign == 'x' else 'Победил O'
#     if mas[0][2] == sign and mas[1][1] == sign and mas[2][0] == sign:
#         return 'Победил X' if sign == 'x' else 'Победил O'
#     if mas[0][0] == sign and mas[1][1] == sign and mas[2][2] == sign:
#         return 'Победил X' if sign == 'x' else 'Победил O'
#     if zeroes == 0:
#         return 'Ничья'
#     return False


# pygame.init()
# size_block = 150
# margin = 15
# width = heigth = size_block*3 + margin*4

# size_window = (width, heigth)
# screen = pygame.display.set_mode(size_window)
# pygame.display.set_caption('Крестики-нолики')

# black = (0, 0, 0)
# red = (232, 39, 55)
# green = (79, 224, 11)
# white = (255, 255, 255)
# gray = (71, 5, 117)
# mas = [[0]*3 for i in range(3)]
# query = 0
# game_over = False

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit(0)
#         elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
#             x_mouse, y_mouse = pygame.mouse.get_pos()
#             col: int = x_mouse // (size_block+margin)
#             row: int = y_mouse // (size_block+margin)
#             if mas[row][col] == 0:
#                 if query % 2 == 0:
#                     mas[row][col] = 'x'
#                 else:
#                     mas[row][col] = 'o'
#                 query += 1
#         elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
#             game_over = False
#             mas = [[0]*3 for i in range(3)]
#             query = 0
#             screen.fill(black)

#     if not game_over:
#         for row in range(3):
#             for col in range(3):
#                 if mas[row][col] == 'x':
#                     color = red
#                 elif mas[row][col] == 'o':
#                     color = green
#                 else:
#                     color = white
#                 x = col*size_block + (col+1)*margin
#                 y = row*size_block + (row+1)*margin
#                 pygame.draw.rect(screen, color, (x, y, size_block, size_block))
#                 if color == red:
#                     pygame.draw.line(screen, white, (x+5, y+5), (x+size_block-5, y+size_block-7), 12)
#                     pygame.draw.line(screen, white, (x+size_block-5, y+5), (x+5, y+size_block-7), 12)
#                 elif color == green:
#                     pygame.draw.circle(screen, white, (x+size_block // 2, y+size_block // 2), size_block // 2-3, 10)
#     if (query-1) % 2 == 0:
#         game_over = check_win(mas, 'x')
#     else:
#         game_over = check_win(mas, 'o')
#     if game_over:
#         screen.fill(gray)
#         font = pygame.font.SysFont('stxingkai', 80)
#         text1 = font.render(game_over, True, red)
#         text_rect = text1.get_rect()
#         text_x = screen.get_width() / 2 - text_rect.width / 2
#         text_y = screen.get_height() / 2 - text_rect.height / 2
#         screen.blit(text1, [text_x, text_y])

#     pygame.display.update()



# №4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.


# def repetition_coding(string: str) -> str:
#     char: str = string[0]
#     count: int | str = 1
#     final_string: str = ''
#     for i in range(1, len(string)):
#         if string[i] == char:
#             count += 1
#         else:
#             if char != string[i]:
#                 if (count == 1 and len(final_string) > 0) and (
#                         not final_string[len(final_string) - 2:-1].isdigit()
#                         or final_string[len(final_string) - 2:-1] == '1'):
#                     count = ''
#             final_string += str(count) + char
#             count = 1
#             char = string[i]
#     final_string += str(count) + char
#     return final_string


# def recovery(string: str) -> str:
#     count: int = 1
#     final_string: str = ''
#     for char in string:
#         if char.isdigit():
#             count = int(char)
#         else:
#             final_string += (char * count)
#     return final_string


# file_path = r'text.txt'

# try:
#     with open(file_path, 'r') as f:
#         text = f.read()
#         if text[0].isdigit():
#             text = recovery(text)
#             with open(file_path, 'w') as file:
#                 file.write(text)
#         else:
#             text = repetition_coding(text)
#             with open(file_path, 'w') as file:
#                 file.write(text)
# except FileNotFoundError:
#     with open(file_path, 'w') as f:
#         f.write(input('Введите строку для шифровки или дешифровки -> '))