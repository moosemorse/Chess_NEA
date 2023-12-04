import pygame 

def drawGameState(screen, state, images, size, validMoves, sqSelected): 
    # Draw squares onto screen 
    drawBoard(screen, size)
    # Highlight squares if needed 
    highlightSquares(screen, state, validMoves, sqSelected, size)
    # Draw pieces ontop of squares 
    drawPieces(screen, state.board, images, size) 

def drawBoard(screen, size): 
    # Light square 
    lightColor = pygame.Color('#595959')
    # Dark square 
    darkColor = pygame.Color('#363636')
    # Iterate through each position on screen
    for row in range(8): 
        for col in range(8): 
            if (row+col)%2 == 0: 
                # Draw light square 
                pygame.draw.rect(screen, lightColor, (col*size, row*size, size, size))
            else: 
                # Draw dark square 
                pygame.draw.rect(screen, darkColor, (col*size, row*size, size, size))

def drawPieces(screen, board, images, size): 
    for row in range(8): 
        for col in range(8): 
            # Get piece at square using 2D array from game state 
            piece = board[row][col] 
            # Check if point is an empty square 
            if piece != "-": 
                screen.blit(images[piece], pygame.Rect(col*size, row*size, size, size))

def highlightSquares(screen, state, validMoves, sqSelected, size): 
    # Make sure a square is selected 
    if sqSelected != (): 
        # Un-pack square selected 
        row, col = sqSelected
        # Check if square is not empty space and if the correct colour piece is selected on user's turn 
        if (state.board[row][col].isupper() ^ state.whiteToMove) and (state.board[row][col] != "-"): 
            # Highlight square of piece 
            highlight = pygame.Surface((size, size))
            # Transparency value 
            highlight.set_alpha(90) 
            # Green circle 
            highlight.fill(pygame.Color('#2c603b'))
            # Draw at position col*size, row*size 
            screen.blit(highlight, (col*size, row*size))
            # Highlight moves from square 
            for move in validMoves: 
                # Check if valid moves corresponding to piece selected 
                if move.startRow == row and move.startCol == col: 
                    # Highlight captures 
                    if state.board[move.endRow][move.endCol] != "-": 
                        highlight.fill(pygame.Color('#d8363c'))
                        screen.blit(highlight, (move.endCol*size, move.endRow*size))
                    else: 
                        # Highlight squares that are valid and empty  
                        highlight.fill(pygame.Color('#ade4bd'))
                        screen.blit(highlight, (move.endCol*size, move.endRow*size))