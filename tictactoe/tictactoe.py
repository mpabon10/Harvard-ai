"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    net = [row.count(X) - row.count(O) for row in board]
    player = X if sum(net) <= 0 else O
    return player


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    openSpaces = set()
    for i in range(len(board)):
        for j in range(len(board[i])):
           if board[i][j] == EMPTY : openSpaces.add((i,j))
    
    return openSpaces

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    
    newBoard = copy.deepcopy(board)
    
    if action not in actions(board) : raise NameError('Action not Available')

    newBoard[action[0]][action[1]] = player(board)
    #print(str(action[0]) + ' ' + str(action[1]))
    #newBoard[action[0]][action[1]] = player(board)
    #print(newBoard)
    return(newBoard)


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    xSpots = set()
    oSpots = set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == X : xSpots.add((i,j))
            if board[i][j] == O : oSpots.add((i,j))
    winSets = [{(0,0),(0,1),(0,2)},
               {(1,0),(1,1),(1,2)},
               {(2,0),(2,1),(2,2)},
               {(0,0),(1,0),(2,0)},
               {(0,1),(1,1),(2,1)},
               {(0,2),(1,2),(2,2)},
               {(0,0),(1,1),(2,2)},
               {(0,2),(1,1),(2,0)}]
    for sets in winSets:
        if sets.issubset(xSpots) : return X
        if sets.issubset(oSpots) : return O
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None : return True
    if len(actions(board)) == 0 : return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X : return 1
    if winner(board) == O : return -1
    return 0

def maxValue(board): 
    """
    Returns highest utilty given a board
    """
    if terminal(board) : return utility(board)

    v = -2

    for action in actions(board) :
        v = max(v, minValue(result(board, action)))

    return v


def minValue(board): 
    """
    Returns lowest utilty given a board
    """
    if terminal(board) : return utility(board)

    v = 2

    for action in actions(board) :
       v = min(v, maxValue(result(board,action)))
        
    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board) : return None

    bestUtility = -2 if player(board) == X else 2
    bestAction = (3,3)

    if player(board) == X :
        for action in actions(board) :
            util = minValue(result(board,action))
            if  util > bestUtility :
                bestUtility = util
                bestAction = action

    else :
        for action in actions(board) :
            util = maxValue(result(board,action))
            if util < bestUtility :
                bestUtility = util
                bestAction = action
    
    return bestAction
