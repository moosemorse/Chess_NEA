import pygame

def draw_buttons(screen, items, object_list, spacing_y, width, font): 
    
    # Calculate positions for buttons
    spacing_x = width // (len(items) + 1)

    # Define button properties
    button_width = 150
    button_height = 50

    for i, text in enumerate(items):
        # Calculate x position for each button
        x = spacing_x * (i + 1) - button_width // 2
        # Calculate y position for row of buttons  
        y = spacing_y + button_height // 2 
        button_rect = pygame.Rect(x, y, button_width, button_height)
        object_list.append((button_rect, text))
        # Draw button rectangle
        pygame.draw.rect(screen, ('#004241'), button_rect)
        # Text drawn onto rectangle 
        text_surface = font.render(text, True, (255, 255, 255)) 
        # Center text 
        text_rect = text_surface.get_rect(center = button_rect.center)
        screen.blit(text_surface, text_rect)

def draw_heading(screen, text, width, spacing_y): 

    font = pygame.font.Font(None, 48) 

    # Center text horizontally  
    x = width // 2 
    # Position text vertically 
    y = spacing_y 

    # Render text 
    text_surface = font.render(text, True, (255,255,255)) 

    # Draw text at coordinates x,y 
    text_rect = text_surface.get_rect(center=(x, y)) 
    screen.blit(text_surface, text_rect) 


def draw_conditions_menu(screen, width, height):
    # Set dark background
    screen.fill((15, 15, 15)) 

    # Set up the font for the button text
    font = pygame.font.Font(None, 24)

    # Vertical spacing between buttons 
    spacing_y = 50 

    """ 

    Side options 

    """

    draw_heading(screen, 'Pick a side', width, spacing_y) 
    spacing_y = spacing_y + 50 

    # Create buttons for colour constraints
    colour_buttons = []
    # Colour options
    colours = ['White', 'Black', 'Random']  

    # Draw time buttons 
    draw_buttons(screen, colours, colour_buttons, spacing_y, width, font) 

    # Increase vertical spacing 
    spacing_y = spacing_y + 150 

    """ 

    Time options 

    """

    draw_heading(screen, 'Time options', width, spacing_y) 
    spacing_y = spacing_y + 50 

    # Create buttons for time constraints
    time_buttons = []
    # Time options
    times = ['1', '5', '10', '15', 'Unlimited']  

    # Draw time buttons 
    draw_buttons(screen, times, time_buttons, spacing_y, width, font) 

    # Increase vertical spacing 
    spacing_y = spacing_y + 150 


    """ 
    
    Difficulty options 

    """

    draw_heading(screen, 'Choose a difficulty', width, spacing_y) 
    spacing_y = spacing_y + 50 
    
    # Create buttons for difficulty options 
    difficulty_buttons = [] 
    # Difficulty options 
    difficulty = ['1', '2', '3']

    # Draw difficulty buttons 
    draw_buttons(screen, difficulty, difficulty_buttons, spacing_y, width, font) 

    # Increase vertical spacing 
    spacing_y = spacing_y + 150 

    """ 
    
    Confirm options 

    """

    # Stores button for 'confirm'
    confirm_button = []
    # Confirm text stored in list 
    confirm = ['Confirm?']   

    # Draw confirm button 
    draw_buttons(screen, confirm, confirm_button, spacing_y, width, font) 

    # Increase vertical spacing 
    spacing_y = spacing_y + 100 

    pygame.display.update()

    return time_buttons

def handle_click(event, time_buttons):
    if event.type == pygame.MOUSEBUTTONDOWN:
        for button_rect, time in time_buttons:
            if button_rect.collidepoint(event.pos):
                # Print the selected time
                print(time)
                return time
    return None