import pygame 

pygame.init() 

def draw_buttons(screen, object_text, object_list, width):

    # Button dimensions 
    button_width = 400 
    button_height = 150 
    # Center buttons
    button_x = width// 2 - button_width//2
    margin = 20 

    # Font 
    font = pygame.font.Font(None, 60) 

    for i, text in enumerate(object_text): 
        button_y = (i*200) + button_height + margin 
        # Draw the button rectangle
        button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
        object_list.append((button_rect, text))
        pygame.draw.rect(screen, (0,65,65), button_rect)
        # Render the text
        text_surface = font.render(text, True, (255,255,255))
        # Calculate the position for the text
        text_rect = text_surface.get_rect(center=button_rect.center)
        # Draw the text over the button
        screen.blit(text_surface, text_rect.topleft)

def draw_sign_out_button(screen, text): 

    font = pygame.font.Font(None, 32) 

    # Dimensions 
    button_width = 50
    button_height = 30

    button_rect = pygame.Rect(30, 150, button_width, button_height) 
    
    # Text drawn onto rectangle 
    text_surface = font.render(text, True, (255, 255, 255)) 

    # Center text 
    text_rect = text_surface.get_rect(topleft = button_rect.topleft)
    screen.blit(text_surface, text_rect) 

    return (button_rect, text)

def drawMainMenu(screen, width, height, username): 
    # Create the main menu window 
    main_menu_surface = pygame.Surface((width, height))
    # Grey color for the window background
    main_menu_surface.fill((15, 15, 15)) 

    # Draw window background 
    screen.blit(main_menu_surface, (0, 0))

    # Stores button tuples for the main three buttons 
    main_buttons = [] 
    # Text drawn onto each button 
    main_text = ['Play', 'Review', 'Rules']

    # Draw buttons 
    draw_buttons(screen, main_text, main_buttons, width) 

    if username == None: 
        draw_text(screen, 'Guest')
        sign_out = draw_sign_out_button(screen, 'Log in')
    else: 
        draw_text(screen, username)
        sign_out = draw_sign_out_button(screen, 'Sign out')

    main_buttons.append(sign_out)

    pygame.display.update() 

    return main_buttons 

def handle_click(main_buttons): 
    # Loop until confirm is True
    run = True 
    while run:
        # Get all events from the event queue
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Handle the quit event to allow the program to exit
                return -1
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if the play button is clicked
                if main_buttons[0][0].collidepoint(event.pos):
                    run = False 
                    return 1
                # Check if review button is clicked
                if main_buttons[1][0].collidepoint(event.pos): 
                    run = False 
                    return 4
                if main_buttons[3][0].collidepoint(event.pos): 
                    run = False 
                    return 6
                

def draw_text(screen, text): 
    # Draw the button rectangle
    button_rect = pygame.Rect(30, 30, 100, 100)
    pygame.draw.rect(screen, (15,15,15), button_rect)
    
    # Create font object
    font = pygame.font.Font(None, 36) 
    
    # Render the text
    text_surface = font.render(text, True, (255,255,255))
    
    # Calculate the position for the text
    text_rect = text_surface.get_rect(center=button_rect.center)
    
    # Draw the text over the button
    screen.blit(text_surface, text_rect.topleft)

