import random

aiChoice = random.randint(0, 2)
choicesFull = ("paper", "rock", "scissors")
choicesLetters = ("p", "r", "s")

wins = 0
losses = 0
ties = 0

print('ROCK, PAPER, SCISSORS')
print(str(wins) + ' Wins, ' + str(losses) + ' Losses, ' + str(ties) + ' Ties')
print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')

#not finished
