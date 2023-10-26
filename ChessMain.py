import pygame  
import ChessEngine
from DrawGameState import drawGameState

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
    while run: 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                run = False 
            # Mouse handler 
            elif event.type == pygame.MOUSEBUTTONDOWN: 
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
                    if move in validMoves: 
                        # Update gamestate by making move 
                        state.makeMove(move) 
                        moveMade = True 
                    # Reset user clicks 
                    sqSelected = () 
                    playerClicks = [] 

            # Key handler 
            elif event.type == pygame.KEYDOWN: 
                # If key 'z' is pressed, execute undoMove 
                if event.key == pygame.K_z: 
                    state.undoMove()
                    moveMade = True  

        if moveMade: 
            validMoves = state.getValidMoves() 
            moveMade = False 

        # Draw the current board 
        drawGameState(screen, state, IMAGES, SQ_SIZE)  
        clock.tick(FPS) 
        pygame.display.flip() 

if __name__ == "__main__": 
    main()

