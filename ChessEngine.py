class GameState(): 
    def __init__(self): 
        # Board representation 
        # Caps represent black pieces e.g 'B' is a black bishop 
        # Lower-caps represent white pieces e.g 'p' is a white pawn 
        self.board = [
            ["R", "N", "B", "Q", "K", "B", "N", "R"],
            ["P", "P", "P", "P", "P", "P", "P", "P"], 
            ["-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-"],
            ["p", "p", "p", "p", "p", "p", "p", "p"],
            ["r", "n", "b", "q", "k", "b", "n", "r"]
        ]
        self.whiteToMove = True 
        self.moveLog = [] 
    
    def makeMove(self, move): 
        # Check if square is empty 
        if self.board[move.startRow][move.startCol] != "-": 
            # Position of piece moved will be empty 
            self.board[move.startRow][move.startCol] = "-"
            # Position piece is moved will have that piece 
            self.board[move.endRow][move.endCol] = move.pieceMoved 
            # Log move 
            self.moveLog.append(move)
            # Switch players 
            self.whiteTomMove = not self.whiteToMove    
    
    def undoMove(self): 
        # Check if 'moveLog' is empty 
        if len(self.moveLog) != 0: 
            # Remove last move and store in move 
            move = self.moveLog.pop() 
            # Update board 
            self.board[move.startRow][move.startCol] = move.pieceMoved 
            self.board[move.endRow][move.endCol] = move.pieceCaptured 
            # Switch players 
            self.whiteToMove = not self.whiteToMove 

    # All moves without considering checks 
    def getMoves(self): 
        moves = []
        # Check each square of 8x8 array 
        for row in range(8): 
            for col in range(8): 
                # Get piece at position of board 
                piece = self.board[row][col]
                # If letter is lower-case, white piece and if it is upper-case, black piece 
                if (piece.islower() and self.whiteToMove) or (piece.isupper() and not self.whiteToMove): 
                    piece = piece.lower() 
                    if piece == "p": 
                        self.getPawnMoves(row, col, moves)
                    elif piece == "r": 
                        self.getRookMoves(row, col, moves) 
        return moves 

    def getPawnMoves(self, row, col, moves): 
        # Check if white pawn is to move 
        if self.whiteToMove: 
            # One square pawn advance 
            if self.board[row-1][col-1] == "-": 
                moves.append(Move((row,col), (row-1,col), self.board))
                # If pawn hasn't moved yet, it can move two squares forward 
                if row == 6 and self.board[row-2][col] == "-":
                    moves.append(Move((row,col), (row-2,col), self.board))

    def getRookMoves(self, row, col, moves): 
        pass 

    # All moves considering checks 
    def getValidMoves(self): 
        # Function will use result from getMoves 
        return self.getMoves() 

class Move(): 
    # Dictionary for mapping values to file/rank notation 
    ranksToRows = {"1": 7, "2": 6, "3": 5, "4": 4, 
                   "5":3, "6":2, "7": 1, "8": 0}
    rowsToRanks = {value: key for key, value in ranksToRows.items()}
    filesToCols = {"a": 0, "b": 1, "c": 2, "d": 3,
                   "e": 4, "f": 5, "g": 6, "h": 7}
    colsToFiles = {value: key for key, value in filesToCols.items()}

    # 'start' - start square and 'end' - end square
    # Passing in 'board' captures updated board 
    def __init__(self, start, end, board): 
        # De-coupling tuples 
        self.startRow = start[0] 
        self.startCol = start[1] 
        self.endRow = end[0] 
        self.endCol = end[1] 
        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceCaptured = board[self.endRow][self.endCol]

    
    # Overriding the equals method 
    # Compare one object with another 
    def __eq__(self, other): 
        # Check if other object is an instance of Move 
        if isinstance(other, Move): 
            return self.getNotation() == other.getNotation()  

    def getNotation(self): 
        return self.getRankFile(self.startRow, self.startCol) + self.getRankFile(self.endRow, self.endCol)
    
    def getRankFile(self, row, col): 
        return self.colsToFiles[col] + self.rowsToRanks[row] 