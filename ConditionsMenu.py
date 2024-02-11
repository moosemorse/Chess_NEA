import pygame
import random 

pygame.init() 

def draw_buttons(screen, items, object_list, spacing_y, width, font, selected): 
    
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
        if text == selected: 
            pygame.draw.rect(screen, ('#00422D'), button_rect)
        else: 
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


def draw_conditions_menu(screen, width, options):
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
    side_buttons = []
    # Colour options
    side = ['White', 'Black', 'Random']  

    # Draw time buttons 
    draw_buttons(screen, side, side_buttons, spacing_y, width, font, options['side']) 

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
    draw_buttons(screen, times, time_buttons, spacing_y, width, font, options['time']) 

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
    draw_buttons(screen, difficulty, difficulty_buttons, spacing_y, width, font, options['diff']) 

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
    draw_buttons(screen, confirm, confirm_button, spacing_y, width, font, None) 

    # Increase vertical spacing 
    spacing_y = spacing_y + 100 

    pygame.display.update()

    return side_buttons, time_buttons, difficulty_buttons, confirm_button

def handle_click(screen, width, side_buttons, time_buttons, diff_buttons, confirm_button):
    confirm = False
    # Options dictionary 
    options = { 
        'side': "White", 
        'time': '1', 
        'diff': '1' 
    }
    # Loop until confirm is True
    while not confirm:
        # Get all events from the event queue
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Handle the quit event to allow the program to exit
                return -1 
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if the click is on the confirm button
                if confirm_button[0][0].collidepoint(event.pos):
                    confirm = True
                    break
                # Otherwise, check the other buttons
                else:
                    buttons_dict = {'side': side_buttons, 'time': time_buttons, 'diff': diff_buttons}
                    for key in buttons_dict:
                        for button_rect, text in buttons_dict[key]:
                            if button_rect.collidepoint(event.pos):
                                # Change the value corresponding to key in dictionary 
                                options[key] = text 
                                draw_conditions_menu(screen, width, options)
                                # Unique case 
                                # Pick a random colour when user clicks random 
                                if text == "Random": 
                                    sides = ["White", "Black"]
                                    # Store randomly selected side in options 
                                    options[key] = random.choice(sides) 
                                if text == "Unlimited": 
                                    options[key] = -1 
    
    # Cast values for compatability with later use 
    if options['side'] == "White": 
        options['side'] = True 
    else: 
        options['side'] = False 
    options['time'] = int(options['time']) * 60   
    options['diff'] = int(options['diff']) - 1                         
                                        
    # Return the selected options                                
    return options 