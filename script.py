#!/usr/bin/env python3

def eggs(someParameter):
    someParameter.append('hello')

spam = [1,2,3]
eggs(spam)
print(spam)

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