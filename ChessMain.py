import pygame  
import ChessEngine
from DrawGameState import drawGameState
import ChessAI
import Timer as t
from EndOfGame import drawEndOfGame, check_end_of_game, play_again
import ConditionsMenu 

# Initalise pygame 
pygame.init() 

# Screen dimensions
HEIGHT = 900  
WIDTH = 1000 
# Move log display box dimensions
MOVE_LOG_WIDTH = 200
MOVE_LOG_HEIGHT = HEIGHT 

# Square dimensions 
SQ_SIZE = 800//8 
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
    buttons = ['resign', 'undo']
    for button in buttons: 
        IMAGES[button] = pygame.image.load(f"assets/main_symbols/{button}.png")
        IMAGES[button] = pygame.transform.scale(IMAGES[button], (80,80)) 

def main(): 
    """ 
    Flags and important initialisations before running while loop 
    """
    # Create screen 
    screen = pygame.display.set_mode((WIDTH, HEIGHT)) 
    clock = pygame.time.Clock()
    screen.fill(pygame.Color("#ebecd0"))

    # Timer 
    timer = t.Timer(300) 
    timer_font = pygame.font.SysFont('Monospace', 26, True, False) 

    # Define game states
    GAME_STATE_MAIN_MENU = 0 
    GAME_STATE_CONDITIONS_MENU = 1
    GAME_STATE_PLAYING = 2

    # Set the initial game state
    game_state = GAME_STATE_CONDITIONS_MENU

    # Move Log Font field  
    moveLogFont = pygame.font.SysFont('Arial', 15, True, False) 

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

    # Flag for end of time reached
    time_end = False

    while run: 
        # Check if it's human's turn by matching booleans 
        humanTurn = (state.whiteToMove and playerOne) or (not state.whiteToMove and playerTwo)
        # Time ends, game ends 
        if timer is not None: 
            if timer.is_time_up() and not gameOver: 
                time_end = True 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                run = False
            # Mouse handler 
            elif event.type == pygame.MOUSEBUTTONDOWN: 
                if humanTurn and not gameOver and game_state == GAME_STATE_PLAYING:
                    # Get location of mouse 
                    location = pygame.mouse.get_pos() 
                    col = location[0]//SQ_SIZE
                    row = location[1]//SQ_SIZE 
                    # Resign button position clicked 
                    if col == 0 and row == 8: 
                        gameOver = True  
                    # Check if mouse position is on chess board 
                    if col <= 7 and row <= 7: 
                        # If human is playing black, we need to flip square selected
                        if playerTwo: 
                            col = 7 - col 
                            row = 7 - row 
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
       
                    # Handle undo event 
                    if col == 1 and row == 8:
                        if humanTurn: 
                            state.undoMove()
                            state.undoMove() 
                            moveMade = True  


        if game_state == GAME_STATE_CONDITIONS_MENU:
            # Draw and interact with the conditions menu
            # Returns buttons created 
            side_buttons, time_buttons, diff_buttons, confirm_button = ConditionsMenu.draw_conditions_menu(screen, WIDTH, HEIGHT)
            # Returns options chosen 
            selected_options = ConditionsMenu.handle_click(event, side_buttons, time_buttons, diff_buttons, confirm_button)

            # Unpacking dictionary 
            if selected_options['side'] == False: 
                # Swap states of playerOne and playerTwo 
                playerOne = not playerOne
                playerTwo = not playerTwo 

            # Re-initalise timer with new timer 
            if selected_options['time'] == -60: 
                timer = None  
                time_left = None 
            else: 
                timer = t.Timer(selected_options['time']) 

            # Change depth level of AI 
            ChessAI.change_depth(selected_options['diff'])


            # Update game state 
            game_state = GAME_STATE_PLAYING
            screen.fill('#ebecd0')

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

        if game_state == GAME_STATE_PLAYING:
            # Draw the current board 
            drawGameState(screen, state, IMAGES, SQ_SIZE, validMoves, sqSelected, playerOne, moveLogFont) 
            if timer is not None: 
                # Draw timer 
                timer.draw(screen, timer_font, 610, 810)  
                time_left = timer.get_total_time() 

        if check_end_of_game(time_end, gameOver, state): 
            gameOver = True 
            # Action is the result of the user clicking a button 
            action = drawEndOfGame(screen, time_left, humanTurn, time_end, state) 
            if action == 'quit': 
                run = False 
            if action == 'play_again': 
                # Pass in ChessEngine, gamestate and timer class 
                state, validMoves, sqSelected, playerClicks, moveMade, gameOver, humanTurn, time_end = play_again(ChessEngine, state)
                if timer is not None: 
                    timer.reset_timer() 

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

