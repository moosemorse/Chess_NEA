import pygame
import pygame.freetype  # Import the freetype module.


pygame.init()

# Store images for read rules section 
IMAGES = {} 

def load_images(): 
    keys = ['chess-basic-movements'] 
    for key in keys: 
        IMAGES[key] = pygame.image.load(f"assets/read_rules_img/{key}.png")
        IMAGES[key] = pygame.transform.scale(IMAGES[key], (500,400))
    return keys 

def draw_images(screen): 
    images = load_images() 
    spacing_y = 20 
    for image in images: 
        screen.blit(IMAGES[image], pygame.Rect(550, spacing_y, 200, 200))
        spacing_y = spacing_y + 400

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
    text_list = ["Under the first image, labelled 'chess movements',", 
                 "each image represents how every piece can move.", 
                 "Don't worry! You can see where pieces move during",
                 "the game through highlighting.", 
                 "Each image has their own label with their own", 
                 "corresponding moves such as the king in the first",
                 "image.",
                 "", 
                 "", 
                 "You will also find the conditions menu when you ", 
                 "press play on the main menu where you can select", 
                 "what options you want to play with.", 
                 "", 
                 "So, for time conditions, each integer represents", 
                 "the time in minutes you will be given for the game.", 
                 "", 
                 "Also, difficulty is ascending so ", 
                 "level 1 is the easiest and level 3 is the hardest.",
                 "", 
                 "", 
                 "Also, review games feature is exclusively for users",
                 "who are logged in! You cannot access it when signed", 
                 "in as guest.",
                 " ", 
                 " ", 
                 "To save games, you just need to press save game at the end of the game you just played and it", 
                 "then should appear in the review games menu when you click on the button.",
                 " ", 
                 " ", 
                 "ENJOY!!"]


    # Drawing the text on the screen 
    for text in text_list: 
        spacing_y = spacing_y + 20 
        text_surface = draw_text(text)
        screen.blit(text_surface, (20, spacing_y))
    
    draw_images(screen) 

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