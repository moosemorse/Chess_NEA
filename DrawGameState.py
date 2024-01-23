import pygame 

def drawGameState(screen, state, images, size, validMoves, sqSelected, white, moveLogFont): 
    # Draw squares onto screen 
    drawBoard(screen, size)
    # Highlight squares if needed 
    highlightSquares(screen, state, validMoves, sqSelected, size, white)
    # Draw pieces ontop of squares 
    drawPieces(screen, state.board, images, size, white) 
    # Draw buttons 
    drawButtons(screen, images )
    # Draw Move Log display 
    drawMoveLog(screen, state, moveLogFont)

def drawButtons(screen, images): 
    # Draw resign flag 
    screen.blit(images['resign'], pygame.Rect(10, 810, 60, 60))
    # Draw undo button 
    screen.blit(images['undo'], pygame.Rect(110, 810, 60, 60))

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

def drawPieces(screen, board, images, size, white): 
    for row in range(8): 
        for col in range(8): 
            # Get piece at square using 2D array from game state 
            if white: 
                piece = board[row][col] 
            else: 
                piece = board[7-row][7-col] 
                # Check if point is an empty square 
            if piece != "-": 
                screen.blit(images[piece], pygame.Rect(col*size, row*size, size, size))

def highlightSquares(screen, state, validMoves, sqSelected, size, white): 
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
            # If white, then draw at col and row 
            # If black we want to draw from 7 - col, 7 - row 
            if white: 
                # Draw at position col*size, row*size 
                screen.blit(highlight, (col*size, row*size))
            else: 
                screen.blit(highlight, ((7-col)*size, (7-row)*size))
            # Highlight moves from square 
            for move in validMoves: 
                # Check if valid moves corresponding to piece selected 
                if move.startRow == row and move.startCol == col: 
                    # Check if user is playing black or white 
                    endCol = move.endCol if white == True else 7 - move.endCol 
                    endRow = move.endRow if white == True else 7 - move.endRow 
                    # Highlight captures 
                    if state.board[move.endRow][move.endCol] != "-": 
                        highlight.fill(pygame.Color('#d8363c'))
                        screen.blit(highlight, (endCol*size, endRow*size))
                    else: 
                        # Highlight squares that are valid and empty  
                        highlight.fill(pygame.Color('#ade4bd'))
                        screen.blit(highlight, (endCol*size, endRow*size))

def drawMoveLog(screen, state, font): 
    # Variable for move log rectangle object 
    moveLogRect = pygame.Rect(800, 0, 200, 1000) 
    pygame.draw.rect(screen, pygame.Color('#ebecd0'), moveLogRect)
    # Store move log list 
    moveLog = state.moveLog
    moveTexts = [] 
    for i in range (0, len(moveLog), 2) : 
        # Format text with index, notation and padding 
        text = str(i//2 + 1) + ".  " + moveLog[i].getNotation() + "  "
        # Check if black has made a move 
        if i + 1 < len(moveLog): 
            text += moveLog[i+1].getNotation() 
        moveTexts.append(text) 
    padding = 10 
    # Y coordinante 
    textY = padding  
    if len(moveTexts) > 0: 
        for i in range(len(moveTexts)): 
            text = moveTexts[i]  
            # Render object 
            textObject = font.render(text, 0, pygame.Color('Black'))
            # Object location  
            textLocation = moveLogRect.move(padding, textY)  
            # Draw object 
            screen.blit(textObject, textLocation) 
            textY += textObject.get_height() + padding