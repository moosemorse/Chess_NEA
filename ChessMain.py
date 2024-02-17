import pygame  
import ChessEngine
from DrawGameState import drawGameState
import ChessAI
import Timer as t
from EndOfGame import drawEndOfGame, check_end_of_game, play_again, get_outcome
import ConditionsMenu
import MainMenu 
import UserManagement 
from datetime import datetime 
import pickle 
import ReviewGamesMenu

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
    GAME_STATE_END = -1 
    GAME_STATE_MAIN_MENU = 0 
    GAME_STATE_CONDITIONS_MENU = 1
    GAME_STATE_PLAYING = 2
    GAME_STATE_SAVE_GAME = 3 
    # For the menu which displays all the games
    GAME_STATE_REVIEW_GAME_MENU = 4 
    # For actually watching the game back 
    GAME_STATE_REVIEWING_GAME = 5 

    # None - user is a guest 
    username = None 

    # Set the initial game state
    game_state = GAME_STATE_MAIN_MENU

    # Move Log Font field  
    moveLogFont = pygame.font.SysFont('Arial', 15, True, False) 

    # Import game state from ChessEngine file 
    state = ChessEngine.GameState() 

    # Create user manager 

    database = "chess_app.db"

    manager = UserManagement.UserManager(database)

    game_saved = False 

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
                                    state.makeMove(screen, validMoves[i]) 
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

        if game_state == GAME_STATE_MAIN_MENU: 
            # Draw and return main menu buttons 
            main_menu_buttons = MainMenu.drawMainMenu(screen, WIDTH, HEIGHT)
            # Handle user clicking which button 
            game_state = MainMenu.handle_click(main_menu_buttons) 


        if game_state == GAME_STATE_CONDITIONS_MENU:
            # Draw and interact with the conditions menu
            # Returns buttons created 
            options = { 
                'side': "White", 
                'time': '1', 
                'diff': '1' 
            }
            side_buttons, time_buttons, diff_buttons, confirm_button = ConditionsMenu.draw_conditions_menu(screen, WIDTH, options)
            # Returns options chosen 
            selected_options = ConditionsMenu.handle_click(screen, WIDTH, side_buttons, time_buttons, diff_buttons, confirm_button)

            if selected_options == -1: 
                game_state = GAME_STATE_END
            else: 
                # Unpacking dictionary 
                if selected_options['side'] == False: 
                    # Set white to False and black to True 
                    playerOne = False 
                    playerTwo = True 
                else: 
                    # Otherwise, user is playing from white so set variables to opposite states 
                    playerOne = True 
                    playerTwo = False 

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
            AIMove = ChessAI.makeBestMove(screen, state, validMoves) 
            if AIMove is None: 
                AIMove = ChessAI.findRandomMove(validMoves) 
            state.makeMove(screen, AIMove, AI = True) 
            moveMade = True 
        

        if moveMade: 
            validMoves = state.getValidMoves() 
            moveMade = False 

        if game_state == GAME_STATE_PLAYING:
            # Reset game_saved variable so user can save game when playing again 
            game_saved = False
            # Draw the current board 
            drawGameState(screen, state, IMAGES, SQ_SIZE, validMoves, sqSelected, playerOne, moveLogFont) 
            if timer is not None: 
                # Draw timer 
                timer.draw(screen, timer_font, 610, 810)  
                time_left = timer.get_total_time() 

        if game_state == GAME_STATE_REVIEW_GAME_MENU: 

            games = manager.get_all_games()
            game_buttons = ReviewGamesMenu.draw_review_games_menu(screen, WIDTH, games)
            game_state = ReviewGamesMenu.handle_click(game_buttons)
            # If the value of game_state is not below, it stores the value of gameID
            if (game_state != -1) and (game_state != 0): 
                gameID = game_state
                game_state = GAME_STATE_REVIEWING_GAME

        if game_state == GAME_STATE_REVIEWING_GAME: 
            # Get clean board
            state = ChessEngine.GameState()
            game_played = manager.get_game(gameID)
 
            drawGameState(screen, state, IMAGES, SQ_SIZE, validMoves, sqSelected, playerOne, moveLogFont)
            

        
        if check_end_of_game(time_end, gameOver, state) and game_state == GAME_STATE_PLAYING: 

            gameOver = True 

            # Serialise moves made (objects) 
            game_played = pickle.dumps(state.moveLog)
            
            outcome, result = get_outcome(humanTurn, time_end, state)
            date_played, time_played = get_date_and_time() 

            history = { 
                'username': username,
                'date': date_played, 
                'time': time_played, 
                'pgn': game_played, 
                'outcome': outcome, 
                'result': result
            }

            # Action is the result of the user clicking a button 
            game_state = drawEndOfGame(screen, time_left, humanTurn, time_end, state) 

            # Save game button pressed 
            if game_state == GAME_STATE_SAVE_GAME and username is not None and game_saved == False: 
                game_saved = manager.save_game(history)
                while game_state == GAME_STATE_SAVE_GAME: 
                    game_state = drawEndOfGame(screen, time_left, humanTurn, time_end, state)
            
            # Reset all attributes 
            state, validMoves, sqSelected, playerClicks, moveMade, gameOver, humanTurn, time_end = play_again(ChessEngine, state)
            if timer is not None: 
                timer.reset_timer() 
        
        if game_state == GAME_STATE_END:
            manager.close_connection()  
            run = False 
            

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

def get_date_and_time(): 
    
    # Get the current date and time
    current_datetime = datetime.now()

    # Separate the date and time
    current_date = current_datetime.date()  
    current_time = current_datetime.time()

    # Format the date and time in the format expected by the database
    formatted_date = current_date.strftime('%Y-%m-%d')  
    formatted_time = current_time.strftime('%H:%M:%S') 

    return formatted_date, formatted_time

if __name__ == "__main__": 
    main()

