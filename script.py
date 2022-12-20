#!/usr/bin/env python3

import sys
while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')

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