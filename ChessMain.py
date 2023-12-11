import pygame  
import ChessEngine
from DrawGameState import drawGameState
import ChessAI

# Initalise pygame 
pygame.init() 

# Screen dimensions
HEIGHT = 800 
WIDTH = 800 

# Square dimensions 
SQ_SIZE = HEIGHT//8 
FPS = 30 
IMAGES = {} 

def loadImages(): 
    # Pass in dictionary to store images 
    pieces = ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R', 'P']
    for piece in pieces:
        # Store black piece 
        IMAGES[piece] = pygame.image.load(f"assets/piece/b_{piece}.png")
        IMAGES[piece] = pygame.transform.scale(IMAGES[piece], (SQ_SIZE,SQ_SIZE))
        # Store white piece 
        IMAGES[piece.lower()] = pygame.image.load(f"assets/piece/w_{piece}.png")
        IMAGES[piece.lower()] = pygame.transform.scale(IMAGES[piece.lower()], (SQ_SIZE,SQ_SIZE))

def main(): 
    # Create screen 
    screen = pygame.display.set_mode((WIDTH, HEIGHT)) 
    clock = pygame.time.Clock()
    screen.fill(pygame.Color("White"))

    # Import game state from ChessEngine file 
    state = ChessEngine.GameState() 
    # Store a list of valid moves 
    validMoves = state.getValidMoves() 
    # Flag variable after a move is made 
    moveMade = False
    # Load all assets into IMAGES dictionary 
    loadImages() 
    # 'sqSelected' keeps track of last position selected by user 
    sqSelected = ()
    # 'playerClicks' keeps track of player clicks, last pos to new pos 
    playerClicks= []
    run = True 
    # If human playing white, this is true. If AI is playing, then false. 
    playerOne = True
    # Same as above but for black 
    playerTwo = False
    # Flag for game over
    gameOver = False  
    while run: 
        # Check if it's human's turn by matching booleans 
        humanTurn = (state.whiteToMove and playerOne) or (not state.whiteToMove and playerTwo)
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                run = False 
            # Mouse handler 
            elif event.type == pygame.MOUSEBUTTONDOWN: 
                if humanTurn and not gameOver: 
                    # Get location of mouse 
                    location = pygame.mouse.get_pos()
                    col = location[0]//SQ_SIZE
                    row = location[1]//SQ_SIZE
                    # Check if user selected same square twice 
                    if sqSelected == (row,col): 
                        # Deselect square and clear player clicks 
                        sqSelected = () 
                        playerClicks = [] 
                    else: 
                        sqSelected = (row, col) 
                        # Append for both 1st and 2nd clicks 
                        playerClicks.append(sqSelected) 
                    # Check if piece has been moved to another square 
                    if len(playerClicks) == 2: 
                        move = ChessEngine.Move(playerClicks[0], playerClicks[1], state.board)
                        # Print notation of move (start --> end)
                        print(move.getNotation())
                        for i in range(len(validMoves)): 
                            if move == validMoves[i]:  
                                # Update gamestate by making move 
                                state.makeMove(validMoves[i]) 
                                moveMade = True 
                                # Reset user clicks if valid move 
                                sqSelected = () 
                                playerClicks = [] 
                        if not moveMade: 
                            # Quicker movement of pieces, if accidentally moved a piece 
                            playerClicks = [sqSelected]
       
            # Key handler 
            elif event.type == pygame.KEYDOWN: 
                # If key 'z' is pressed, execute undoMove 
                if event.key == pygame.K_z: 
                    if humanTurn: 
                        state.undoMove()
                        state.undoMove() 
                        moveMade = True  
                # Reset the board when 'r' is pressed 
                if event.key == pygame.K_r: 
                    state = ChessEngine.GameState() 
                    validMoves = state.getValidMoves() 
                    sqSelected = () 
                    playerClicks = [] 
                    moveMade = False 

        # AI moves 
        if not humanTurn and not gameOver: 
            AIMove = ChessAI.makeBestMove(state, validMoves) 
            if AIMove is None: 
                AIMove = ChessAI.findRandomMove(validMoves) 
            state.makeMove(AIMove, AI = True) 
            moveMade = True 
        

        if moveMade: 
            validMoves = state.getValidMoves() 
            moveMade = False 

        # Draw the current board 
        drawGameState(screen, state, IMAGES, SQ_SIZE, validMoves, sqSelected) 

        if state.checkmate: 
            # End of game, so set flag as true 
            gameOver = True 
            drawText(screen, 'checkmate')
        elif state.stalemate: 
            gameOver = True 
            drawText(screen, 'stalemate')

        clock.tick(FPS) 
        pygame.display.flip() 

def drawText(screen, text): 
    # Font of text 
    font = pygame.font.SysFont('Monospace', 26, True, False) 
    # Render object 
    textObject = font.render(text, 0, pygame.Color('Blue'))
    # Center object 
    textLocation = pygame.Rect(0,0, WIDTH, HEIGHT).move(WIDTH/2 - textObject.get_width()/2, HEIGHT/2 - textObject.get_height()/2)
    # Draw object 
    screen.blit(textObject, textLocation) 

if __name__ == "__main__": 
    main()

