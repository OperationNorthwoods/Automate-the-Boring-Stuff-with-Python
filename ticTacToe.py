# ch 5, tic tac toe , not finished. started using the books data structure but am trying the user input on my own

theBoard4 = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
             'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
             'low-L': ' ', 'low-M': ' ', 'low-R': ' ',
             'board': [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']],}
theBoard3 = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']]
theBoard2 = [['top-L', 'top-M', 'top-R',
             'mid-L', 'mid-M', 'mid-R',
              'low-L', 'low-M', 'low-R'],
             [' ', ' ', ' ',
              ' ', ' ', ' ',
              ' ', ' ', ' ',]]
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}


def printBoard(board):
    print('      L | M | R   ')
    print('      =========')
    print('Top | ' + board['top-L'] + ' | ' + board['top-M'] + ' | ' + board['top-R'])
    print('    | --+---+--')
    print('Mid | ' + board['mid-L'] + ' | ' + board['mid-M'] + ' | ' + board['mid-R'])
    print('    | --+---+--')
    print('Low | ' + board['low-L'] + ' | ' + board['low-M'] + ' | ' + board['low-R'])


def isWinner(board):
    for i in range(9):
        streak = 0
        streak += 1
        # if streak =

# board[1][i]


print('Welcome, this is Tic Tac Toe.')
while True:
    printBoard(theBoard)
    while True:
        player_move = input('Make your Move. Use format "row-COLUMN". Example: top-L')
        player_move_location = input()

# giving up for now, will be way more time consuming than originally thought
