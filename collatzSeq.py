# this is a practice project at the end of chapter 3
import time

def collatz(number):
    if number % 2 == 0:
        return number // 2
    else: 
        return 3 * number + 1


try:
    print('Enter Number:')
    num = int(input())
    while num != 1:
        time.sleep(0.1) # increasing legibility
        num = collatz(num)
        print(num)
except ValueError:
    print('Must enter a valid integer!')

# no errors