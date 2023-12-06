import random 

# Values of pieces 
pieceScore = {"K": 20000, "Q": 900, "R": 500, "B": 330, "N": 320, "P": 100}

""" 
piece-square table values for each piece represented as a 2D array 
"""
pieceSquare = {"K": [
    [-30,-40,-40,-50,-50,-40,-40,-30,]
    [-30,-40,-40,-50,-50,-40,-40,-30,]
    [-30,-40,-40,-50,-50,-40,-40,-30,]
    [-30,-40,-40,-50,-50,-40,-40,-30,]
    [-20,-30,-30,-40,-40,-30,-30,-20,]
    [-10,-20,-20,-20,-20,-20,-20,-10,]
    [20, 20,  0,  0,  0,  0, 20, 20, ]
    [ 20, 30, 10,  0,  0, 10, 30, 20]], 
               "Q": [
    [-20,-10,-10, -5, -5,-10,-10,-20,]
    [-10,  0,  0,  0,  0,  0,  0,-10,]
    [-10,  0,  5,  5,  5,  5,  0,-10,]
    [ -5,  0,  5,  5,  5,  5,  0, -5,]
    [  0,  0,  5,  5,  5,  5,  0, -5,]
    [-10,  5,  5,  5,  5,  5,  0,-10,]
    [-10,  0,  5,  0,  0,  0,  0,-10,]
    [-20,-10,-10, -5, -5,-10,-10,-20]], 
               "R": [
    [-40, -25, -25, -25, -25, -25, -25, -40,]
    [-30, 0, 0, 0, 0, 0, 0, -30,]
    [-30, 0, 0, 0, 0, 0, 0, -30,]
    [-30, 0, 0, 15, 15, 0, 0, -30,]
    [-30, 0, 0, 15, 15, 0, 0, -30,]
    [-30, 0, 10, 0, 0, 10, 0, -30,]
    [-30, 0, 0, 5, 5, 0, 0, -30,]
    [-40, -30, -25, -25, -25, -25, -30, -40]], 
               "B":[
    [-20,-10,-10,-10,-10,-10,-10,-20,]
    [-10,  0,  0,  0,  0,  0,  0,-10,]
    [-10,  0,  5, 10, 10,  5,  0,-10,]
    [-10,  5,  5, 10, 10,  5,  5,-10,]
    [-10,  0, 10, 10, 10, 10,  0,-10,]
    [-10, 10, 10, 10, 10, 10, 10,-10,]
    [-10,  5,  0,  0,  0,  0,  5,-10,]
    [-20,-10,-10,-10,-10,-10,-10,-20]] , 
               "N":[
    [-50,-40,-30,-30,-30,-30,-40,-50,]
    [-40,-20,  0,  0,  0,  0,-20,-40,]
    [-30,  0, 10, 15, 15, 10,  0,-30,]
    [-30,  5, 15, 20, 20, 15,  5,-30,]
    [-30,  0, 15, 20, 20, 15,  0,-30,]
    [-30,  5, 10, 15, 15, 10,  5,-30,]
    [-40,-20,  0,  5,  5,  0,-20,-40,]
    [-50,-40,-30,-30,-30,-30,-40,-50]] , 
               "P": [ 
    [0,  0,  0,  0,  0,  0,  0,  0,]
    [50, 50, 50, 50, 50, 50, 50, 50,]
    [10, 10, 20, 30, 30, 20, 10, 10,]
    [5,  5, 10, 25, 25, 10,  5,  5,]
    [0,  0,  0, 20, 20,  0,  0,  0,]
    [5, -5,-10,  0,  0,-10, -5,  5,]
    [5, 10, 10,-20,-20, 10, 10,  5,]
    [0,  0,  0,  0,  0,  0,  0,  0]], 
               }
# Checkmate score 
CHECKMATE = 100000 
# Stalemate score 
STALEMATE = 0 

def findRandomMove(validMoves): 
    # Generate random index 
    position = random.randint(0, len(validMoves)-1) 
    # Return move from valid moves 
    return validMoves[position]

def scoreMaterial(board): 
    materialScore = 0 
    # Iterate through each square on board 
    for row in board: 
        for square in row: 
            if square != "-": 
                # If piece is white, add score from pieceScores
                if square.islower(): 
                    materialScore += pieceScore[square.upper()]
                # If piece is black, subtract score from pieceScores
                elif square.isupper(): 
                    materialScore -= pieceScore[square.upper()]
    return materialScore 

def scorePosition(board): 
    positionScore = 0 
    # Iterate through each square on board 
    for row in board: 
        for square in row: 
            if square != "-": 
                # If piece is white, we add bonus from piece-square tables 
                if square.islower(): 
                    positionScore += pieceSquare[square.upper()][row][square]
                # If piece is white, we add bonus from piece-square tables 
                elif square.isupper(): 
                    positionScore -= pieceSquare[square.upper()][row][square]
    return positionScore

def scoreBoard(state): 
    pass 
