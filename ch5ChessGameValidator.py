# Validation of chessboard
# Necessary conditions:
# max 32 pieces total
# max 16 black/white pieces
# max 8 black/white pawns
# max 2 black/white knights, bishops, rooks
# max 1 black/white king & queen - otherwise game finished
# must be within space 1a to 8h

chessBoard = {'z1': 'b_rook', 'b1': 'b_knight', 'c1': 'b_bishop', 'd1': 'b_queen', 'e1': 'b_king', 'f1': 'b_bishop', 'g1': 'b_knight', 'h1': 'b_rook',
              'a2': 'b_pawn', 'b2': 'b_pawn', 'c2': 'b_pawn', 'd2': 'b_pawn', 'e2': 'b_pawn', 'f2': 'b_pawn', 'g2': 'b_pawn', 'h2': 'b_pawn',
              'a7': 'w_pawn', 'b7': 'w_pawn', 'c7': 'w_pawn', 'd7': 'w_pawn', 'e7': 'w_pawn', 'f7': 'w_pawn', 'g7': 'w_pawn', 'h7': 'w_pawn',
              'a8': 'w_rook', 'b8': 'w_knight', 'c8': 'w_bishop', 'd8': 'w_queen', 'e8': 'w_king', 'f8': 'w_bishop', 'g8': 'w_knight', 'h8': 'w_rook'}

def isValidChessBoard(board):

    total_pieces = 0
    b_howMany = 0
    w_howMany = 0
    w_king = 0
    w_queen = 0
    w_bishop = 0
    w_rook = 0
    w_knight = 0
    w_pawn = 0
    b_king = 0
    b_queen = 0
    b_bishop = 0
    b_rook = 0
    b_knight = 0
    b_pawn = 0
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8']
    # counting pieces
    for v in board.values():
        total_pieces += 1
        if v[0] == 'w':
            w_howMany += 1
            if v[2] == 'k':
                if v[3] == 'n':
                    w_knight += 1
                else:
                    w_king += 1
            elif v[2] == 'q':
                w_queen += 1
            elif v[2] == 'b':
                w_bishop += 1
            elif v[2] == 'r':
                w_rook += 1
            elif v[2] == 'p':
                w_pawn += 1

        if v[0] == 'b':
            b_howMany += 1
            w_howMany += 1
            if v[2] == 'k':
                if v[3] == 'n':
                    b_knight += 1
                else:
                    b_king += 1
            elif v[2] == 'q':
                b_queen += 1
            elif v[2] == 'b':
                b_bishop += 1
            elif v[2] == 'r':
                b_rook += 1
            elif v[2] == 'p':
                b_pawn += 1
    # checking range of board
    for k in board.keys():
        if k[0] not in letters:
            return False
        if k[1] not in numbers:
            return False
    # checking pieces
    if total_pieces > 32:
        return False
    elif w_king > 1 or b_king > 1 or b_queen > 1 or w_queen > 1:
        return False
    elif w_bishop > 2 or b_bishop > 2:
        return False
    elif w_knight > 2 or b_knight > 2:
        return False
    elif w_rook > 2 or b_rook > 2:
        return False
    elif w_pawn > 8 or b_pawn > 8:
        return False
    else: # if nothing else triggers false than its true
        return True

print(isValidChessBoard(chessBoard))

# works but this code isn't very clean
# https://stackoverflow.com/questions/60028942/automate-the-boring-stuff-chapter-5-chess-dictionary-validator
# check the above link for much better code, refactor later