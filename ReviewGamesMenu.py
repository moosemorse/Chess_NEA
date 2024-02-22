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

def draw_return_button(screen, button_list, font): 
    
    # Dimensions 
    spacing_x = 75
    button_width = 100
    button_height = 100 
    x = spacing_x - (button_width // 2) 
    y = 0

    # Purpose and text displayed on button 
    text = "Main menu"

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

    draw_return_button(screen, buttons, font) 

    for game in games:  

        # Draw time buttons 
        draw_buttons(screen, width, game, buttons, spacing_y, font) 

        # Increase vertical spacing 
        spacing_y = spacing_y + 150 

        pygame.display.update()

    return buttons

def handle_click(buttons):

    while True: 
        # Get all events from the event queue
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Handle the quit event to allow the program to exit
                return -1 
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if a button (game) has been clicked
                    for button in buttons: 
                        button_rect, text = button
                        if button_rect.collidepoint(event.pos):
                            if text == "Main menu":
                                # Return back to main menu so value of GAME_STATE_MAIN_MENU
                                return 0 
                            else: 
                                # If the button pressed is not "Go back" 
                                # It has to be a game, so text is the GameID which we return 
                                return text  
                             
def draw_move_buttons(screen, button_list, font): 

    # Static dimensions 
    button_width = 100
    button_height = 100
    y = 800  

    # Calculate positions for buttons - center horizontally 
    spacing_x = 800 // 3   

    # Draw 2 buttons 
    for i in range(0,2):    
        x = spacing_x * (i + 1) - button_width // 2

        # Purpose and text displayed on button 
        if i == 0: 
            text = "Move back" 
        else: 
            text = "Move forward"

        button_rect = pygame.Rect(x, y, button_width, button_height) 
        button_list.append((button_rect, text)) 

        # Text drawn onto rectangle 
        text_surface = font.render(text, True, (255, 255, 255)) 

        # Center text 
        text_rect = text_surface.get_rect(center = button_rect.center)
        screen.blit(text_surface, text_rect)

def draw_reviewing_buttons(screen): 

    # No screen fill because this is drawn over game (drawGameState) 
    # Buttons for moving back, moving forward, returning back to main menu 
    buttons = [] 

    # Set up the font for the button text
    font = pygame.font.Font(None, 32)

    draw_move_buttons(screen, buttons, font)

    draw_return_button(screen, buttons, font) 

    return buttons 

def handle_click_reviewing(buttons): 
    
    while True: 
        # Get all events from the event queue
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Handle the quit event to allow the program to exit
                return -1 
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if a button (game) has been clicked
                    for button in buttons:
                        button_rect, text = button 
                        if button_rect.collidepoint(event.pos):
                            if text == "Main menu":
                                # Return back to main menu so value of GAME_STATE_MAIN_MENU
                                return 0 
                            elif text == "Move forward": 
                                return '1'
                            else:
                                return '-1'
                             
if __name__ == '__main__': 

    # Initalise pygame 
    pygame.init() 

    # Screen dimensions
    HEIGHT = 900  
    WIDTH = 1000 
    # Move log display box dimensions

    # Create screen 
    screen = pygame.display.set_mode((WIDTH, HEIGHT)) 
    clock = pygame.time.Clock()

    run = True 
    
    games = [] 

    while run: 

        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                run = False
            else: 
                buttons = draw_reviewing_buttons(screen) 

        clock.tick(60) 
        pygame.display.flip()