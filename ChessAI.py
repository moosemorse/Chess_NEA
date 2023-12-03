import random 

def findRandomMove(validMoves): 
    # Generate random index 
    position = random.randint(0, len(validMoves)-1) 
    # Return move from valid moves 
    return validMoves[position]