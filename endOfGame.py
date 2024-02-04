import pygame 

def draw_button(screen, text, x, y, width, height):
    # Draw the button rectangle
    button_rect = pygame.Rect(x, y, width, height)
    pygame.draw.rect(screen, (0,65,65), button_rect)
    
    # Create font object
    font = pygame.font.Font(None, 36) 
    
    # Render the text
    text_surface = font.render(text, True, (255,255,255))
    
    # Calculate the position for the text
    text_rect = text_surface.get_rect(center=button_rect.center)
    
    # Draw the text over the button
    screen.blit(text_surface, text_rect.topleft)
    
    return button_rect

def draw_text(screen, text, x, y, width, height): 
    # Draw the button rectangle
    button_rect = pygame.Rect(x, y, width, height)
    pygame.draw.rect(screen, (15,15,15), button_rect)
    
    # Create font object
    font = pygame.font.Font(None, 36) 
    
    # Render the text
    text_surface = font.render(text, True, (255,255,255))
    
    # Calculate the position for the text
    text_rect = text_surface.get_rect(center=button_rect.center)
    
    # Draw the text over the button
    screen.blit(text_surface, text_rect.topleft)

def get_outcome(human_turn, time_end, state): 
    # Time ran out 
    if time_end: 
        return "LOST", "lost by time." 
    
    # Check whether human lost or won 
    if not human_turn: 
        if state.checkmate: 
            return "LOST", "lost by checkmate." 
    else: 
        if state.checkmate: 
            return "WON", "won by checkmate." 
    
    # Stalemate is a draw 
    if state.stalemate: 
        return "DRAW", "have stalemated." 
    
    # Last case is a resignation 
    return "LOST", "resigned." 

def check_end_of_game(time_end, gameOver, state): 
    # Return true if any of the variables are true 
    return time_end or gameOver or state.stalemate or state.checkmate 

def play_again(ChessEngine, state): 
    # Reset values of variables 
    state = ChessEngine.GameState() 
    validMoves = state.getValidMoves() 
    sqSelected =() 
    playerClicks = [] 
    moveMade = False 
    gameOver = False 
    humanTurn = True 
    time_end = False
    return state, validMoves, sqSelected, playerClicks, moveMade, gameOver, humanTurn, time_end


def drawEndOfGame(screen, time_left, human_turn, time_end, state): 
    # Constants
    BOARD_WIDTH = 800
    BOARD_HEIGHT = 800
    # Width of the end-of-game window
    WINDOW_WIDTH = 400
    # Height of the end-of-game window
    WINDOW_HEIGHT = 600 

    # Center the end-of-game window
    window_x = (BOARD_WIDTH - WINDOW_WIDTH) // 2
    window_y = (BOARD_HEIGHT - WINDOW_HEIGHT) // 2

    # Create the end-of-game window
    end_game_surface = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
    # Grey color for the window background
    end_game_surface.fill((15, 15, 15)) 

    # Draw window background 
    screen.blit(end_game_surface, (window_x, window_y))

    # Height of each button
    button_height = 40 
    # Space between buttons
    button_margin = 20 

    # Calculate the starting y position of the first button
    button_y = window_y + button_margin

    # Outcome of player and reason 
    outcome, reason = get_outcome(human_turn, time_end, state)

    # Draw buttons/text 

    # End of game state text 
    draw_text(screen, f'{outcome}', window_x + WINDOW_WIDTH//4, button_y, WINDOW_WIDTH//2, button_height)
    # Update button_y for the next button
    button_y += button_height + button_margin

    # Cause of loss text  
    draw_text(screen, f'You {reason}', window_x + WINDOW_WIDTH//4, button_y, WINDOW_WIDTH//2, button_height)
    # Update button_y for the next button
    button_y += button_height + button_margin

    if time_left != None: 
        # Time left text 
        draw_text(screen, f'Time left: {time_left}', window_x + WINDOW_WIDTH//4, button_y, WINDOW_WIDTH//2, button_height)
        # Update button_y for the next button
        button_y += button_height + button_margin

    # Play again button 
    play_again_button = draw_button(screen, 'Play again', window_x + WINDOW_WIDTH//4, button_y, WINDOW_WIDTH//2, button_height)
    # Update button_y for the next button
    button_y += button_height + button_margin
    
    # Main menu button 
    main_menu_button = draw_button(screen, 'Main menu', window_x + WINDOW_WIDTH//4, button_y, WINDOW_WIDTH//2, button_height)
    # Update button_y for the next button
    button_y += button_height + button_margin

    # Save game button 
    save_game_button = draw_button(screen, 'Save game', window_x + WINDOW_WIDTH//4, button_y, WINDOW_WIDTH//2, button_height)
    # Update button_y for the next button
    button_y += button_height + button_margin

    # Main window loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return 'quit' 
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if the play again button was clicked
                if play_again_button.collidepoint(event.pos):
                    return 'play_again'

        pygame.display.flip()