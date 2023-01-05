#!/usr/bin/env python3

import copy, sys, time, random, pprint, pyperclip

# testing command line arguments

arg_test0 = sys.argv[0]
arg_test1 = sys.argv[1]
arg_test2 = sys.argv[2]

print(f"This is your 0th cmd line arg: {arg_test0}")
print(f"This is your 1st cmd line arg: {arg_test1}")
print(f"This is your 2nd cmd line arg: {arg_test2}")
print(sys.argv)


# pieces = ['king', 'queen', 'rook', 'knight', 'bishop', 'pawn']
# colors = ['b', 'w']
# all_pieces = set(color+piece for piece in pieces for color in colors)

# print(all_pieces)

# chessBoard = {'a1': 'b_rook', 'b1': 'b_knight', 'c1': 'b_bishop', 'd1': 'b_queen', 'e1': 'b_king', 'f1': 'b_bishop', 'g1': 'b_knight', 'h1': 'b_rook',
#               'a2': 'b_pawn', 'b2': 'b_pawn', 'c2': 'b_pawn', 'd2': 'b_pawn', 'e2': 'b_pawn', 'f2': 'b_pawn', 'g2': 'b_pawn', 'h2': 'b_pawn',
#               'a7': 'w_pawn', 'b7': 'w_pawn', 'c7': 'w_pawn', 'd7': 'w_pawn', 'e7': 'w_pawn', 'f7': 'w_pawn', 'g7': 'w_pawn', 'h7': 'w_pawn',
#               'a8': 'w_rook', 'b8': 'w_knight', 'c8': 'w_bishop', 'd8': 'w_queen', 'e8': 'w_king', 'f8': 'w_bishop', 'g8': 'w_knight', 'h8': 'w_rook'}

# for k in chessBoard.keys():
#     print(f'k={k}')
# for v in chessBoard.values():
#     print(f'v={v}')

# message = "It was a bright cold day in April, and the clocks were striking thirteen."
# count = {}

# for character in message:
#     count.setdefault(character, 0)
#     count[character] +=1

# pprint.pprint(count)

# just debugging ch4CoinFlipStreaks.py here
# tenK_List = []
# generated_list = []
# numberOfStreaks = 0


# for y in range(10000):
#     streak_counter = 0
#     streak_letter = ''
#     for x in range(100):
#         counter = x
#         if random.randint(0, 1) == 0:
#             generated_list.append('H')
#         else:
#             generated_list.append('T')
#         if counter == 99:
#             tenK_List.append(generated_list.copy())
#             generated_list = []
# # print(generated_list)
# # print(tenK_List)
#     for x in range(100):
#         if x == 0:
#             streak_letter = tenK_List[y][x]
#         if streak_letter == tenK_List[y][x]:
#             streak_counter += 1
#             if streak_counter == 6:
#                 print('STREAKKKK!!!!!!!!!')
#                 numberOfStreaks += 1
#                 streak_counter = 0
#         else:
#             streak_counter = 0
#             streak_letter = tenK_List[y][x]
#         print(streak_counter, end=' | ')
#         print(streak_letter, end='')
#     time.sleep(0.1)
#     print('There are '+str(numberOfStreaks)+' Streaks so far.')



# def eggs(someParameter):
#     someParameter.append('hello')

# spam = [1,2,3]
# eggs(spam)
# print(spam)

# print("Column 1", end="\t")
# print("Column 2")

# def spam(divideBy):
#     return 42 / divideBy

# try:
#     print(spam(2))
#     print(spam(12))
#     print(spam(0))
#     print(spam(1))
# except ZeroDivisionError:
#         print('Error: Invalid Argument')

# def spam():
#     global eggs
#     eggs = 'spam'

# def bacon():
#     eggs = 'bacon'

# def ham():
#     print(eggs)

# eggs = 42
# spam()
# bacon()
# ham()
# print(eggs)

# def spam():
#     global eggs
#     eggs = 'spam'
# eggs = 'global'
# spam()
# print(eggs)

# def hello(name):
#     print('Hello, ' + name)

# hello('Alice')
# hello('Bob')

# num = 0
# while num < 10:
#     num += 1
#     print(num)

# for i in range(1, 11):
#     print(i)

# spam = input()
# if spam == '1':
#     print('hello')
# elif spam == '2':
#     print('howdy')
# else:
#     print('Greetings!')

# import sys
# while True:
#     print('Type exit to exit.')
#     response = input()
#     if response == 'exit':
#         sys.exit()
#     print('You typed ' + response + '.')

# import random
# for i in range(5):
#     print(random.randint(1, 10))

# while True:
#     print('Who are you??')
#     name = input()
#     if name != 'Joe':
#         continue
#     print('Hello, Joe Blow. What is the password? (it is a fish)')
#     password = input()
#     if password == 'swordfish':
#         break
# print('Access Granted.')

# name = ''
# while True:
#     print('Please Type Your Name')
#     name = input()
#     if name == 'your name':
#         break
# print('Thank you!!!')

# name = 'Carol'
# age = 3000
# if name == 'Alice':
#     print('Hi, Alice')
# elif age < 12:
#     print('You are not Alice, kiddo.')
# elif age > 2000:
#     print('Unlike you, Alice is not an undead immortal Vampire.')
# elif age > 100:
#     print('You are not Alice, grannie.')


# print('Hello world!')
# print('What is your name?')
# myName = input()
# print('It is good to meet you, ' + myName)
# print('The length of your name is:')
# print(len(myName))
# print('What is your age?')
# myAge = input()
# print('You will be ' + str(int(myAge) + 1)+ ' in a year.')