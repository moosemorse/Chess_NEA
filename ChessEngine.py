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
        self.moveFunctions = {'p': self.getPawnMoves, 'r': self.getRookMoves, 'n': self.getKnightMoves, 
                              'b': self.getBishopMoves, 'q': self.getQueenMoves, 'k': self.getKingMoves}
        self.whiteKingLocation = (7,4) 
        self.blackKingLocation = (0,4) 
        self.inCheck = False 
        self.pins = [] 
        self.checks = [] 
        self.checkMate = False
        self.staleMate = False
        self.enPassantPossible = () 
        self.currentCastlingRights = CastleRights(True, True, True, True) 
        self.castleRightsLog = [CastleRights(self.currentCastlingRights.wks, self.currentCastlingRights.bks, 
                                             self.currentCastlingRights.wqs, self.currentCastlingRights.bqs)] 
        
    
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
            self.whiteToMove = not self.whiteToMove 

            # Update the King's location if moved 
            if move.pieceMoved == "k": 
                self.whiteKingLocation = (move.endRow, move.endCol) 
            if move.pieceMoved == "K": 
                self.blackKingLocation = (move.endRow, move.endCol)

            # Pawn promotion 
            if move.isPawnPromotion:
                # All pieces player can promote to 
                validPieces = ('q', 'n', 'r', 'b')
                while True:
                    promotedPiece = input("Select which piece to promote to ('Q', 'N', 'R', 'B'): ").lower()
                    if promotedPiece in validPieces:
                        # Because self.whiteToMove switched earlier in algorithm  
                        if self.whiteToMove:
                            # Black piece 
                            promotedPiece = promotedPiece.upper()
                        self.board[move.endRow][move.endCol] = promotedPiece
                        break
                    else:
                        print("Please choose 'q', 'n', 'r', or 'b'.")
    
            # En Passant 
            if move.isEnPassant: 
                # Capture pawn 
                self.board[move.startRow][move.endCol] = '-' 

            # Update enpassantPossible 
            if move.pieceMoved.lower() == 'p' and abs(move.startRow-move.endRow) == 2:
                self.enPassantPossible = ((move.startRow + move.endRow)//2, (move.startCol))
            else: 
                self.enPassantPossible = () 

            # Castle Move 
            if move.isCastleMove: 
                # Kingside castle 
                if move.endCol - move.startCol == 2: 
                    # Move rook 
                    self.board[move.startRow][move.endCol - 1] = self.board[move.startRow][move.endCol + 1] 
                    # Remove rook from initial positon 
                    self.board[move.startRow][move.endCol + 1] = "-"
                # Queenside castle 
                else: 
                    # Move rook 
                    self.board[move.startRow][move.endCol + 1] = self.board[move.startRow][move.endCol-2]
                    # Remove rook from initial positon 
                    self.board[move.startRow][move.endCol - 2] = "-"

            
            # Handle castle rights 
            self.updateCastleRights(move) 
            self.castleRightsLog.append(CastleRights(self.currentCastlingRights.wks, self.currentCastlingRights.bks, 
                                             self.currentCastlingRights.wqs, self.currentCastlingRights.bqs))

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

            # Update the King's location if moved 
            if move.pieceMoved == "k": 
                self.whiteKingLocation = (move.startRow, move.startCol) 
            if move.pieceMoved == "K": 
                self.blackKingLocation = (move.startRow, move.startCol) 

            # Undo En Passant 
            if move.isEnPassant: 
                self.board[move.endRow][move.endCol] = "-"
                self.board[move.startRow][move.endCol] = move.pieceCaptured 
                self.enPassantPossible = (move.endRow, move.endCol) 

            # Undo 2 square pawn advance 
            if move.pieceMoved.lower() == 'p' and abs(move.startRow - move.endRow) == 2: 
                self.enPassantPossible = () 

            # Undo castle rights 
            self.castleRightsLog.pop()  
            self.currentCastlingRights = self.castleRightsLog[-1]

            # Undo castle move 
            if move.isCastleMove: 
                # Kingside castle 
                if move.endCol - move.startCol == 2: 
                    # Move rook 
                    self.board[move.startRow][move.endCol + 1] = self.board[move.startRow][move.endCol - 1] 
                    # Remove rook from initial positon 
                    self.board[move.startRow][move.endCol - 1] = "-"
                # Queenside castle 
                else: 
                    # Move rook 
                    self.board[move.startRow][move.endCol - 2] = self.board[move.startRow][move.endCol + 1]
                    # Remove rook from initial positon 
                    self.board[move.startRow][move.endCol + 1] = "-"
    
    # Update castle rights given move 

    def updateCastleRights(self, move): 
        if move.pieceMoved == 'k': 
            self.currentCastlingRights.wks = False 
            self.currentCastlingRights.wqs = False
        elif move.pieceMoved == 'K': 
            self.currentCastlingRights.bks = False
            self.currentCastlingRights.bqs = False 
        elif move.pieceMoved == 'r': 
            # Looking at left rook 
            if move.startRow == 7 and move.startCol == 0: 
                self.currentCastlingRights.wqs = False
            # Looking at right rook 
            else: 
                self.currentCastlingRights.wks = False
        elif move.pieceMoved == 'R': 
            # Looking at left rook 
            if move.startRow == 0 and move.startCol == 0: 
                self.currentCastlingRights.bqs = False
            # Looking at right rook 
            else: 
                self.currentCastlingRights.bks = False

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
                    # Calls the appropiate function depending on the piece type 
                    self.moveFunctions[piece](row, col, moves)
        return moves 

    def getPawnMoves(self, row, col, moves): 
        piecePinned = False 
        pinDirection = () 
        # Iterate backwards through pins 
        for i in range(len(self.pins)-1, -1 , -1): 
            # Check if pawn is a pinned piece 
            if self.pins[i][0] == row and self.pins[i][1] == col: 
                piecePinned = True 
                # Save direction it is pinned from 
                pinDirection = (self.pins[i][2], self.pins[i][3])
                self.pins.remove(self.pins[i])
                break 
        
        # Check if white pawn is to move 
        if self.whiteToMove: 
            # One square pawn advance 
            if self.board[row-1][col] == "-": 
                # Check if piece is pinned or the pin direction is in the direction of piece movement 
                if not piecePinned or pinDirection == (-1, 0): 
                    moves.append(Move((row,col), (row-1,col), self.board))
                    # If pawn hasn't moved yet, it can move two squares forward 
                    if row == 6 and self.board[row-2][col] == "-":
                        moves.append(Move((row,col), (row-2,col), self.board))

            # Check if pawn is not on edge of screen 
            if col-1 >= 0:
                # Check if piece diagonally to left is black 
                if self.board[row-1][col-1].isupper(): 
                    # Check if piece is pinned 
                    if not piecePinned or pinDirection == (-1, -1): 
                        # Pawn can capture piece 
                        moves.append(Move((row, col), (row-1, col-1), self.board)) 
                elif (row-1, col-1) == self.enPassantPossible: 
                    # Check if piece is pinned 
                    if not piecePinned or pinDirection == (-1, -1):
                        # En Passant capture 
                        moves.append(Move((row,col), (row-1, col-1), self.board, isEnPassant=True))


            if col+1 <= 7: 
                if self.board[row-1][col+1].isupper():
                    if not piecePinned or pinDirection == (-1, 1): 
                        moves.append(Move((row, col), (row-1, col+1), self.board)) 
                elif (row-1, col+1) == self.enPassantPossible: 
                    # Check if piece is pinned 
                    if not piecePinned or pinDirection == (-1, 1):
                        # En Passant capture 
                        moves.append(Move((row,col), (row-1, col+1), self.board, isEnPassant=True))    

        # Check if black pawn is to move 
        else:  
            # One square pawn advance 
            if self.board[row+1][col] == "-": 
                if not piecePinned or pinDirection == (1, 0):
                    moves.append(Move((row,col), (row+1,col), self.board))
                    # If pawn hasn't moved yet, it can move two squares forward 
                    if row == 1 and self.board[row+2][col] == "-":
                        moves.append(Move((row,col), (row+2,col), self.board))

            # Check if pawn is not on edge of screen 
            if col-1 >= 0:
                # Check if piece diagonally to left is black 
                if self.board[row+1][col-1].islower(): 
                    if not piecePinned or pinDirection == (1, -1): 
                        # Pawn can capture piece 
                        moves.append(Move((row, col), (row+1, col-1), self.board)) 
                elif (row+1, col-1) == self.enPassantPossible: 
                    # Check if piece is pinned 
                    if not piecePinned or pinDirection == (1, -1):
                        # En Passant capture 
                        moves.append(Move((row,col), (row+1, col-1), self.board, isEnPassant=True))

            if col+1 <= 7: 
                if self.board[row+1][col+1].islower(): 
                    if not piecePinned or pinDirection == (1,1): 
                        moves.append(Move((row, col), (row+1, col+1), self.board)) 
                elif (row+1, col+1) == self.enPassantPossible: 
                    # Check if piece is pinned 
                    if not piecePinned or pinDirection == (1, 1):
                        # En Passant capture 
                        moves.append(Move((row,col), (row+1, col+1), self.board, isEnPassant=True))

    def getRookMoves(self, row, col, moves): 
        piecePinned = False 
        pinDirection = () 
        for i in range(len(self.pins)-1, -1, -1): 
            if self.pins[i][0] == row and self.pins[i][1] == col: 
                piecePinned = True 
                pinDirection = (self.pins[i][2], self.pins[i][3])
                # Can't remove queen from pin on rook moves, only remove it on bishop moves 
                if self.board[row][col].lower() != "q":
                    self.pins.remove(self.pins[i])
                break 

        # Different directions rook can move up, left, down, right 
        directions = ((-1,0), (0,-1), (1,0), (0,1)) 
        # Iterate through each direction 
        for d in directions: 
            # Check 1-7 rows and columns 
            for i in range(1,8): 
                # Check for each square on file and rank 
                endRow = row + d[0]*i 
                endCol = col + d[1]*i 
                # Check if on board 
                if (0 <= endRow < 8) and (0 <= endCol < 8): 
                    if not piecePinned or pinDirection == d or pinDirection  == (-d[0], -d[1]): 
                        endPiece = self.board[endRow][endCol] 
                        # Rook can move to empty space 
                        if endPiece == "-": 
                            moves.append(Move((row, col), (endRow, endCol), self.board))
                        # Rook can take enemy piece 
                        elif endPiece.islower() ^ self.whiteToMove: 
                            moves.append(Move((row, col), (endRow, endCol), self.board))
                            break 
                        # Case for friendly case which breaks loop 
                        else: 
                            break 
                # Case for off board which breaks loop 
                else: 
                    break 

    def getKnightMoves(self, row, col, moves): 
        piecePinned = False
        for i in range(len(self.pins)-1, -1, -1): 
            if self.pins[i][0] == row and self.pins[i][1] == col:
                piecePinned = True 
                self.pins.remove(self.pins[i]) 
                break 

        # Knight moves in L-shapes 
        directions = ((-2,-1), (-2,1), (-1,-2), (-1,2), (1,-2), (1,2), (2,-1), (2,1)) 
        for d in directions: 
            # Check for each 'L' shape away from the knight
            endRow = row + d[0] 
            endCol = col + d[1] 
            # Check if on board 
            if (0 <= endRow < 8) and (0 <= endCol < 8):
                if not piecePinned: 
                    endPiece = self.board[endRow][endCol] 
                    # Empty square 
                    if endPiece == "-": 
                            moves.append(Move((row, col), (endRow, endCol), self.board))
                    # Square with opponent piece 
                    elif endPiece.islower() ^ self.whiteToMove: 
                            moves.append(Move((row, col), (endRow, endCol), self.board))
                        
    def getBishopMoves(self, row, col, moves): 
        piecePinned = False 
        pinDirection = () 
        for i in range(len(self.pins)-1, -1, -1): 
            if self.pins[i][0] == row and self.pins[i][1] == col: 
                piecePinned = True 
                pinDirection = (self.pins[i][2], self.pins[i][3])
                self.pins.remove(self.pins[i])
                break 

        directions = ((-1,-1), (-1, 1), (1, -1), (1,1)) 
        for d in directions: 
            # Check 1-7 rows and columns 
            for i in range(1,8): 
                # Check for each square on file and rank 
                endRow = row + d[0]*i 
                endCol = col + d[1]*i 
                # Check if on board 
                if (0 <= endRow < 8) and (0 <= endCol < 8): 
                    if (not piecePinned) or (pinDirection == d) or (pinDirection  == (-d[0], -d[1])): 
                        endPiece = self.board[endRow][endCol] 
                        # Bishop can move to empty space 
                        if endPiece == "-": 
                            moves.append(Move((row, col), (endRow, endCol), self.board))
                        # Bishop can take enemy piece 
                        elif endPiece.islower() ^ self.whiteToMove: 
                            moves.append(Move((row, col), (endRow, endCol), self.board))
                            break 
                        # Case for friendly case which breaks loop 
                        else: 
                            break 
                # Case for off board which breaks loop 
                else: 
                    break 

    def getQueenMoves(self, row, col, moves): 
        # Queen moves like a rook and bishop combined 
        self.getRookMoves(row, col, moves)
        self.getBishopMoves(row, col, moves) 

    def getKingMoves(self, row, col, moves): 
        directions = ((-1,-1), (-1,0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1,1)) 
        # Check each tuple within directions 
        for d in directions: 
            endRow = row + d[0] 
            endCol = col + d[1] 
            # Check if on board 
            if (0 <= endRow < 8) and (0 <= endCol < 8):
                endPiece = self.board[endRow][endCol]  
                # Check if empty space or enemy piece 
                if (endPiece == "-") or (endPiece.islower() ^ self.whiteToMove): 
                    if self.whiteToMove: 
                        self.whiteKingLocation = (endRow, endCol) 
                    else: 
                        self.blackKingLocation = (endRow, endCol) 
                    # Function returns three outputs 
                    inCheck, _, _ = self.checkForPinsAndCheck()
                    # Check if (endRow, endCol) would leave king vulnerable, if not add to moves 
                    if not inCheck: 
                        moves.append(Move((row,col), (endRow, endCol), self.board)) 
                    # Place black king back on original location 
                    if self.whiteToMove: 
                        self.whiteKingLocation = (row, col) 
                    else: 
                        self.blackKingLocation = (row, col) 
            self.getCastleMoves(row, col, moves) 
        
        """ 
        Generate all valid castle moves for the king at (r,c) and add them to list of moves 
        """

    def getCastleMoves(self, row, col, moves): 
        # Can't castle if king in check 
        if not(self.inCheck): 
            print("Not in check") 
            # Check black/white castle king side 
            if(self.whiteToMove and self.currentCastlingRights.wks) or (not self.whiteToMove and self.currentCastlingRights.bks): 
                self.getKingsideCastleMoves(row, col, moves)
            # Check black/white castle queen side 
            if(self.whiteToMove and self.currentCastlingRights.wqs) or (not self.whiteToMove and self.currentCastlingRights.bks): 
                self.getQueensideCastleMoves(row, col, moves) 

    def getKingsideCastleMoves(self, row, col, moves): 
        # Can only castle if there are no pieces between rook and king 
        if self.board[row][col+1] == '-' and self.board[row][col+2] == '-': 
            # Need to check if square that king moves to will be attacked 
            # Flag - tracks if king is checked on any squared 
            check = False 
            # Iterate for values of i = 1,2 
            for i in range(1,3): 
                # If white's turn, check white king 
                if self.whiteToMove: 
                    self.whiteKingLocation = (row, col + i) 
                    # inCheck for that particular square (row, col + i) 
                    print("Here - checkForPinsAndCheck") 
                    inCheck, pins, checks = self.checkForPinsAndCheck()
                    print(check) 
                    if inCheck: 
                        print("Check == True")
                        print(check) 
                        check = True 
                    self.whiteKingLocation = (row, col) 
                else: 
                    self.blackKingLocation = (row, col + i) 
                    # inCheck for that particular square (row, col + i) 
                    inCheck, pins, checks = self.checkForPinsAndCheck()
                    if inCheck: 
                        check = True 
                    # Reset kings location 
                    self.blackKingLocation = (row, col) 
            if check == False: 
                moves.append(Move((row, col), (row, col +2), self.board, isCastleMove = True)) 

    def getQueensideCastleMoves(self, row, col, moves): 
        # Can only castle if there are no pieces between rook and king 
        if self.board[row][col-1] == '-' and self.board[row][col-2] == '-' and self.board[row][col-3] == "-": 
            # Need to check if square that king moves to will be attacked 
            # Flag - tracks if king is checked on any squared 
            check = False 
            # Iterate for values of i = 1,2 
            for i in range(1,3): 
                # If white's turn, check white king 
                if self.whiteToMove: 
                    self.whiteKingLocation = (row, col - i) 
                    # inCheck for that particular square (row, col - i) 
                    inCheck, pins, checks = self.checkForPinsAndCheck()
                    if inCheck == True: 
                        check = True 
                    self.whiteKingLocation = (row, col) 
                else: 
                    self.blackKingLocation = (row, col - i) 
                    # inCheck for that particular square (row, col - i) 
                    inCheck, pins, checks = self.checkForPinsAndCheck()
                    if inCheck == True: 
                        check = True 
                    # Reset kings location 
                    self.blackKingLocation = (row, col) 
            if check == False: 
                moves.append(Move((row, col), (row, col - 2), self.board, isCastleMove = True))

    # All moves considering checks 
    def getValidMoves(self): 
        moves = [] 
        self.inCheck, self.pins, self.checks = self.checkForPinsAndCheck() 
        if self.whiteToMove: 
            # Unpack tuple 
            kingRow = self.whiteKingLocation[0] 
            kingCol = self.whiteKingLocation[1] 
        else: 
            kingRow = self.blackKingLocation[0] 
            kingCol = self.blackKingLocation[1] 
        # Check if king is in check, if not, all moves are valid 
        if self.inCheck: 
            # Check if only one check, so either block check or move king 
            if len(self.checks) == 1: 
                # Generate possible moves 
                moves = self.getMoves() 
                # Extract check information 
                check = self.checks[0]
                checkRow = check[0] 
                checkCol = check[1] 
                # Enemy piece causing check 
                pieceChecking = self.board[checkRow][checkCol]
                # Squares that pieces can move to 
                validSquares = [] 
                # If pieceChecking is a knight, then either capture piece or move king 
                if pieceChecking.lower() == 'n': 
                    validSquares = [(checkRow, checkCol)]
                else:
                    for i in range(1,8): 
                        # Check[2] and check[3] are the check directions 
                        validSquare = (kingRow + check[2] * i, kingCol + check[3] * i)
                        validSquares.append(validSquare)
                        # Finish once you get to piece and check
                        if validSquare[0] == checkRow and validSquare[1] == checkCol: 
                            break 
                # Get rid of any moves that don't block check or move king 
                # Go through backwards when you are removing from a list 
                for i in range(len(moves) -1 , -1, -1): 
                    # Move doesn't move king so it must block or capture 
                    if moves[i].pieceMoved[0].lower() != 'k': 
                        # Move doesn't block check or capture piece 
                        if not (moves[i].endRow, moves[i].endCol) in validSquares: 
                            moves.remove(moves[i]) 

            # Case: double-check and king has to move 
            else: 
                self.getKingMoves(kingRow, kingCol, moves) 
        # Not in check at all so all moves are fine 
        else: 
            moves = self.getMoves() 
        
        # Either checkmate or stalemate 
        if len(moves) == 0: 
            if self.inCheck: 
                self.checkMate = True
            else: 
                self.staleMate = True 
        else: 
            self.checkMate = False 
            self.staleMate = False 

        return moves 
    
    def checkForPinsAndCheck(self): 
        # Squares where the allied pinned piece is and direction pinned from 
        pins = [] 
        # Squares where enemy is applying a check 
        checks = [] 
        inCheck = False 
        # If white turn, check white king 
        if self.whiteToMove: 
            startRow = self.whiteKingLocation[0] 
            startCol = self.whiteKingLocation[1] 
        # If black turn, check black king 
        else: 
            startRow = self.blackKingLocation[0] 
            startCol = self.blackKingLocation[1]
        #Check outward from king for pins and checks, keep track of pins 
        directions = ((-1,0), (0,-1), (1,0), (0,1), (-1,-1), (-1,1), (1,-1), (1,1))
        for i in range(len(directions)): 
            d = directions[i] 
            # Reset possible pins 
            possiblePin = () 
            for j in range(1,8): 
                endRow = startRow + d[0] * j 
                endCol = startCol + d[1] * j 
                if (0 <= endRow < 8) and (0 <= endCol < 8): 
                    endPiece = self.board[endRow][endCol] 
                    # Check if ally piece and that piece is not a king 
                    if (endPiece.isupper() ^ self.whiteToMove) and (endPiece.lower() != "k") and (endPiece.lower() != "-"): 
                        # First allied piece could be pinned 
                        if possiblePin == (): 
                            possiblePin = (endRow, endCol, d[0], d[1]) 
                        else: 
                            break 
                    # Case for enemy piece 
                    elif not(endPiece.isupper() ^ self.whiteToMove) and (endPiece.lower() != "-"): 
                        """ 
                        1) Check for all directions of Rook and Bishop directions 
                        2) Check if piece is a queen or if a king is one space away 
                        3) Check if piece is a pawn and validate directions it can attack according to its colour 
                        """
                        if ((0 <= i <= 3) and (endPiece.lower() == "r")) or ((4 <= i <= 7) and (endPiece.lower() == "b")) or \
                        (endPiece.lower() == "q") or (j == 1 and endPiece.lower() == "k") or \
                        (endPiece.lower() == "p" and j == 1 and (((endPiece.isupper() and self.whiteToMove) and 4 <= i <= 5) or (endPiece.islower() and not(self.whiteToMove) and 6 <= i <=7))):
                            # No piece blocking, so it would be a direct check  
                            if possiblePin == (): 
                                inCheck = True
                                checks.append((endRow, endCol, d[0], d[1]))
                                break 
                            # Piece blocking, so there's a pin 
                            else: 
                                pins.append(possiblePin) 
                                break 
                        # Case: there are no checks 
                        else: 
                            break 
                # Case: off board         
                else: 
                    break
                
        # Check for knight checks 
        knightMoves = ((-2,-1), (-2,1), (-1,-2), (-1,2), (1,-2), (1,2), (2,-1), (2,1)) 
        for k in knightMoves: 
            endRow = startRow + k[0] 
            endCol = startCol + k[1] 
            # Check if on board 
            if (0 <= endRow < 8) and (0 <= endCol < 8 ): 
                endPiece = self.board[endRow][endCol] 
                # Check if if piece is enemy and is a knight 
                if (endPiece.islower() ^ self.whiteToMove) and (endPiece.lower() == "n"): 
                    inCheck = True 
                    checks.append((endRow, endCol, k[0], k[1]))    
        return inCheck, pins, checks 
    
class CastleRights(): 
    
    def __init__(self, wks, bks, wqs, bqs): 
        self.wks = wks 
        self.bks = bks 
        self.wqs = wqs 
        self.bqs = bqs 


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
    def __init__(self, start, end, board, isEnPassant = False, isCastleMove = False): 
        # De-coupling tuples 
        self.startRow = start[0] 
        self.startCol = start[1] 
        self.endRow = end[0] 
        self.endCol = end[1] 
        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceCaptured = board[self.endRow][self.endCol]
        self.isPawnPromotion = False 
        # E.g black pawn travels down board, reaching last row (endRow == 7), pawn is on back rank 
        if (self.pieceMoved == "P" and self.endRow == 7) or (self.pieceMoved == "p" and self.endRow == 0): 
            self.isPawnPromotion = True 
        # En  Passant case 
        self.isEnPassant = isEnPassant
        if self.isEnPassant: 
            self.pieceCaptured = 'P' if self.pieceMoved.islower() else 'p'
        # Castle move 
        self.isCastleMove = isCastleMove 


    
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