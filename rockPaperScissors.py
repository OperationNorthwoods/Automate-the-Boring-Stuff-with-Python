import random, sys

choicesFull = ('PAPER', 'ROCK', 'SCISSORS')
choicesLetter = ('p', 'r', 's', 'q')

wins = 0
losses = 0
ties = 0


def update_score(x, y):  # x is player and y is AI
    global wins
    global losses
    global ties
    if x == y:                   # Tie
        print('It is a tie!')
        ties += 1
    elif x == 'r' and y == 's':  # winners
        print('You win!')
        wins += 1
    elif x == 'p' and y == 'r':
        print('You win!')
        wins += 1
    elif x == 's' and y == 'p':
        print('You win!')
        wins += 1
    elif x == 'r' and y == 'p':  # losers
        print('You Lost!')
        losses += 1
    elif x == 'p' and y == 'p':
        print('You Lost!')
        losses += 1
    elif x == 's' and y == 'r':
        print('You Lost!')
        losses += 1


print('ROCK, PAPER, SCISSORS')
while True: # main game loop
    print(str(wins) + ' Wins, ' + str(losses) +
          ' Losses, ' + str(ties) + ' Ties')
    while True: # player input loop
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit()
        elif playerMove == 'r' or playerMove == 'p' or playerMove == 's' or playerMove == 'q':
            break
        print('please make a valid choice!')

    if playerMove == 'r':
        print('ROCK versus...')
        num = random.randint(0, 2)
        aiMove = choicesLetter[num]
        print(str(choicesFull[num]))
        update_score(playerMove, aiMove)
    elif playerMove == 'p':
        print('Paper versus...')
        num = random.randint(0, 2)
        aiMove = choicesLetter[num]
        print(str(choicesFull[num]))
        update_score(playerMove, aiMove)
    elif playerMove == 's':
        print('SCISSORS versus...')
        num = random.randint(0, 2)
        aiMove = choicesLetter[num]
        print(str(choicesFull[num]))
        update_score(playerMove, aiMove)

# no errors