import pygame 

""" drawGameState function allows us to add later improvements like piece highlighting """
def drawGameState(screen, state, images, size): 
    # Draw squares onto screen 
    drawBoard(screen, size)
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

