import pygame 

def draw_button(screen, text, x, y, width, height):
    # Draw the button rectangle
    button_rect = pygame.Rect(x, y, width, height)
    pygame.draw.rect(screen, (50,50,50), button_rect)
    
    # Create font object
    font = pygame.font.Font(None, 36) 
    
    # Render the text
    text_surface = font.render(text, True, (200,0,200))
    
    # Calculate the position for the text
    text_rect = text_surface.get_rect(center=button_rect.center)
    
    # Draw the text over the button
    screen.blit(text_surface, text_rect.topleft)
    
    return button_rect


def drawEndOfGame(screen): 
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

    # Draw buttons

    # Play again button 
    play_again_button = draw_button(screen, 'Play again', window_x + WINDOW_WIDTH//4, button_y, WINDOW_WIDTH//2, button_height)
    # Update button_y for the next button
    button_y += button_height + button_margin

    # Main window loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if the play again button was clicked
                if play_again_button.collidepoint(event.pos):
                    print("play again click")

        pygame.display.flip()