import pygame

def draw_buttons(screen, width, game_record, button_list, spacing_y, font): 
    
    # Calculate positions for buttons
    spacing_x = width // 2
    # Define button properties
    button_width = 700
    button_height = 100 

    # Unpack tuple (which is record)
    gameID, username, datePlayed, TimePlayed, GamePlayed, outcome, reason = game_record 
    text = outcome + "     " + reason + "     " + datePlayed + "     " + TimePlayed

    # Calculate x position for button - center button 
    x = spacing_x - button_width // 2
    # Calculate y position for button  
    y = spacing_y + button_height // 2 

    # Instantiate button
    button_rect = pygame.Rect(x, y, button_width, button_height)
    button_list.append((button_rect, gameID))
    pygame.draw.rect(screen, ('#004241'), button_rect)

    # Text drawn onto rectangle 
    text_surface = font.render(text, True, (255, 255, 255)) 

    # Center text 
    text_rect = text_surface.get_rect(center = button_rect.center)
    screen.blit(text_surface, text_rect)

def draw_return_button(screen, button_list, spacing_y, font): 
    
    # Dimensions 
    spacing_x = 50 
    button_width = 100
    button_height = 100 
    spacing_y = spacing_y // 2 
    x = spacing_x - (button_width // 2) 
    y = spacing_y + (button_height // 2) 

    # Purpose and text displayed on button 
    text = "Go back"

    button_rect = pygame.Rect(x, y, button_width, button_height) 
    button_list.append((button_rect, text)) 

    # Text drawn onto rectangle 
    text_surface = font.render(text, True, (255, 255, 255)) 

    # Center text 
    text_rect = text_surface.get_rect(center = button_rect.center)
    screen.blit(text_surface, text_rect) 


def draw_review_games_menu(screen, width, games):
    # Set dark background
    screen.fill((15, 15, 15)) 

    # Set up the font for the button text
    font = pygame.font.Font(None, 32)

    # Vertical spacing between buttons 
    spacing_y = 50 

    # List that stores button objects
    buttons = []

    draw_return_button(screen, buttons, spacing_y, font) 

    for game in games:  

        # Draw time buttons 
        draw_buttons(screen, width, game, buttons, spacing_y, font) 

        # Increase vertical spacing 
        spacing_y = spacing_y + 150 

        pygame.display.update()

    return buttons

def handle_click(buttons):

    # Get all events from the event queue
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Handle the quit event to allow the program to exit
            return -1 
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if a button (game) has been clicked
                for button in buttons:
                    for button_rect, text in button:
                        if button_rect.collidepoint(event.pos):
                             if text == "Go back":
                                 # Return back to main menu so value of GAME_STATE_MAIN_MENU
                                 return 0 
                             else: 
                                 # If the button pressed is not "Go back" 
                                 # It has to be a game, so text is the GameID which we return 
                                 return text  