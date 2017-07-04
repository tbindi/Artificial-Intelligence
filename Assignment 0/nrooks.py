# nrooks.py : Solve the N-Rooks problem!
# D. Crandall, August 2016
#
# The N-rooks problem is: Given an empty NxN chessboard, place N rooks on the
# board so that no rooks
# can take any other, i.e. such that no two rooks share the same row or column.

# This is N, the size of the board.
N = 220


# Count # of pieces in given row
def count_on_row(board, row):
    return sum(board[row])


def check_piece_queen(hashMap):
    flag = True
    key_list = list(hashMap)
    for i in range(0, len(key_list)):
        for j in range(i+1, len(key_list)):
            if key_list[i][0] == key_list[j][0] or key_list[i][1] == \
                    key_list[j][1]:
                flag = False
                break
            elif abs(key_list[i][0] - key_list[j][0]) == abs(key_list[i][1] -\
                    key_list[j][1]):
                flag = False
                break
    return flag


# Check if the particular row and column is safe from other queens
def check_piece(hashMap, row, col):
    flag = True
    for key, value in hashMap.iteritems():
        if key[0] == row or key[1] == col:
            flag = False
            break
        elif abs(key[0] - row) == abs(key[1] - col):
            flag = False
            break
    return flag


# Count # of pieces in given column
def count_on_col(board, col):
    return sum([row[col] for row in board])


# Count total # of pieces on board
def count_pieces(board):
    return sum([sum(row) for row in board])


# Return a string with the board rendered in a human-friendly format
def printable_board(board):
    return "\n".join([" ".join(["Q" if col else "_" for col in row])
                      for row in board])


# Add a piece to the board at the given position, and return a new board
# (doesn't change original)
def add_piece(board, row, col):
    return board[0:row] + [board[row][0:col] + [1, ] + board[row][col+1:]] + \
           board[row+1:]


# Get list of successors of given board state
def successors(board):
    return [add_piece(board, r, c) for r in
            range(0, N) for c in range(0, N)]


# To overcome:
# 1. states that have N+1 rooks on them
# 2. allowing "moves" that involve not adding a rook at all
def successors2(board):
    return [add_piece(board, r, c) for r in
            range(0, N) for c in range(0, N) if board[r][c] != 1 and
            count_pieces(add_piece(board, r, c)) <= N]


# Loads the location of the queens/rooks on to a hash map for faster processing
def load_hashmap(board):
    return {(x,board[x].index(1)): 1 for x in range(0, N) if count_on_row(
        board, x) >= 1}


# New Abstraction
def successors3(board):
    result = []
    for r in range(0, N):
        if count_on_row(board, r) >= 1:
            continue
        for c in range(0, N):
            if count_on_col(board, c) >= 1:
                continue
            if count_pieces(add_piece(board, r, c)) <= N and board[r][c] != 1:
                y = add_piece(board, r, c)
                result.append(y)
                # Break after new rook finds it's first comfortable
                # position.
                # Don't store all the states unless it's required. (DFS)
                break
    return result


# New Abstraction
def successors_queen(board):
    result = []
    hashMap = load_hashmap(board)
    for r in range(0, N):
        if count_on_row(board, r) >= 1:
            continue
        for c in range(0, N):
            if count_on_col(board, c) >= 1:
                continue
            if count_pieces(add_piece(board, r, c)) <= N and board[r][c] != 1\
                    and check_piece(hashMap, r, c):
                    y = add_piece(board, r, c)
                    result.append(y)
                    # Break after new rook finds it's first comfortable
                    # position.
                    # Don't store all the states unless it's required. (DFS)
                    break
    return result


# check if board is a goal state
def is_goal(board):
    return count_pieces(board) == N and \
        all([count_on_row(board, r) <= 1 for r in range(0, N)]) and \
        all([count_on_col(board, c) <= 1 for c in range(0, N)])


# Check if board is a goal state for N-Queens
def is_goal_queen(board):
    return count_pieces(board) == N and \
           all([count_on_row(board, r) <= 1 for r in range(0, N)]) and \
           all([count_on_col(board, c) <= 1 for c in range(0, N)]) and \
           check_piece_queen(load_hashmap(board))


# Solve n-rooks!
def solve(initial_board):
    fringe = [initial_board]
    while len(fringe) > 0:
        v = fringe.pop()
        for s in successors3(v):
            if is_goal(s):
                return s
            fringe.append(s)
    return False


# The board is stored as a list-of-lists. Each inner list is a row of the board.
# A zero in a given square indicates no piece, and a 1 indicates a piece.
initial_board = [[0]*N]*N
print "Starting from initial board:\n" + printable_board(initial_board) +\
      "\n\nLooking for solution...\n"
solution = solve(initial_board)
print printable_board(solution) if solution else "Sorry, no solution found. :("
