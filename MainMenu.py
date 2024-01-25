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


def drawEndOfGame(screen, width, height, time_left, human_turn, time_end, state): 
    # Create the end-of-game window
    end_game_surface = pygame.Surface((width, height))
    # Grey color for the window background
    end_game_surface.fill((15, 15, 15)) 

    # Draw window background 
    screen.blit(end_game_surface, (0, 0))

    # Window y starting coordinate 
    window_y = 0 
    # Height of each button
    button_height = 40 
    # Space between buttons
    button_margin = 20 

    # Calculate the starting y position of the first button
    button_y = window_y + button_margin


    # Main window loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Event handler for clicking buttons 
                pass 
        
        pygame.display.flip() 