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

    # Load all assets into IMAGES dictionary 
    loadImages() 

    run = True 
    while run: 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                run = False 
        
        # Draw the current board 
        drawGameState(screen, state, IMAGES, SQ_SIZE)  
        clock.tick(FPS) 
        pygame.display.flip() 

if __name__ == "__main__": 
    main()

