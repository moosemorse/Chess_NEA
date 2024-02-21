import pygame
import pygame.freetype  # Import the freetype module.


pygame.init()

def draw_text(text): 
    game_font = pygame.freetype.SysFont("monospace", 16) 
    text_surface, rect = game_font.render(text, (255,255,255))

    return text_surface  

def draw_return_button(screen, button_list): 
    
    # Set up the font for the button text
    font = pygame.font.Font(None, 32)

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

def display_rules_window(screen):

    # Fill screen with dark colour background 
    screen.fill((15,15,15))

    # Stores all buttons, which on this menu is only for a main menu button
    button_list = []

    draw_return_button(screen, button_list)
        
    # spacing_y tracks value at y position text is drawn
    spacing_y = 75

    # Text drawn on each line 
    text_list = ['Hello', 'World']

    # Drawing the text on the screen 
    for text in text_list: 
        spacing_y = spacing_y + 20 
        text_surface = draw_text(text)
        screen.blit(text_surface, (20, spacing_y))

    pygame.display.update()

    return button_list



def handle_click(buttons): 
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1 
            
            elif event.type == pygame.MOUSEBUTTONDOWN: 
                for button in buttons: 
                    # Unpack element into button rect and text
                    button_rect, button_text = button
                    # Check if the user clicked the current button 
                    if button_rect.collidepoint(event.pos): 
                        if button_text == "Main menu": 
                            # Game state value for main menu
                            return 0 