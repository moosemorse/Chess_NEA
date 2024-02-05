import pygame 

def draw_buttons(screen, object_text, object_list, width):

    # Button dimensions 
    button_width = 250 
    button_height = 250 
    # Center buttons
    button_x = width // 2 
    # Padding from top of window 
    button_y = 10 

    # Font 
    font = pygame.font.Font(None, 60) 

    for i, text in enumerate(object_text): 
        button_y = (i*50) + button_y 
        # Draw the button rectangle
        button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
        object_list.append((button_rect, text))
        pygame.draw.rect(screen, (0,65,65), button_rect)
        # Render the text
        text_surface = font.render(object_text, True, (255,255,255))
        # Calculate the position for the text
        text_rect = text_surface.get_rect(center=button_rect.center)
        # Draw the text over the button
        screen.blit(text_surface, text_rect.topleft)

def drawMainMenu(screen, width, height): 
    # Create the main menu window 
    main_menu_surface = pygame.Surface((width, height))
    # Grey color for the window background
    main_menu_surface.fill((15, 15, 15)) 

    # Draw window background 
    screen.blit(main_menu_surface, (0, 0))

    # Stores button tuples for the main three buttons 
    main_buttons = [] 
    # Text drawn onto each button 
    main_text = ['Play', 'Review', 'Read']

    # Draw buttons 
    draw_buttons(screen, main_text, main_buttons, width) 

    pygame.display.update() 

    return main_buttons 

