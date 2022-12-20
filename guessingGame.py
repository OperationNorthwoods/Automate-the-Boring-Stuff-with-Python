import random

howManyGuesses = 0
print('I am thinking of a number between 1 and 20')
number = random.randint(1, 20)

while True:
    print('Take a guess.')
    guess = int(input())
    if guess < number:
        print('Your guess is too low')
        howManyGuesses += 1
    elif guess > number:
        print('Your guess is too high')
        howManyGuesses += 1
    else:
        howManyGuesses += 1
        break
print('Good Job! You guessed my number in ' + str(howManyGuesses) + ' guesses.')

#no errors