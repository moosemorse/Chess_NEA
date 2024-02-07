import pygame

pygame.init() 

PROMOTION_IMAGES = {}

def loadImages():
    # Pass in dictionary to store images 
    pieces = ['R', 'N', 'B', 'Q']
    for piece in pieces:
        # Store black piece 
        PROMOTION_IMAGES[piece] = pygame.image.load(f"assets/piece/b_{piece}.png")
        PROMOTION_IMAGES[piece] = pygame.transform.scale(PROMOTION_IMAGES[piece], (80,80))
        # Store white piece 
        PROMOTION_IMAGES[piece.lower()] = pygame.image.load(f"assets/piece/w_{piece}.png")
        PROMOTION_IMAGES[piece.lower()] = pygame.transform.scale(PROMOTION_IMAGES[piece.lower()], (80,80))

def draw_buttons(screen, player_is_white, object_list, width):

    # Button dimensions 
    button_width = 90  
    button_height = 90 
    # Center buttons 
    button_x = width//2 - button_width//2 
    margin = 10 

    # Load white images if user is playing from white perspective 
    # Else load the black pieces since the user is playing from black's perspective 

    if player_is_white: 
        pieces = ['r', 'n', 'b', 'q']
    else: 
        pieces = ['R', 'N', 'B', 'Q'] 

    for i, piece in enumerate(pieces): 
        button_y = (i*50) + button_height + margin 
        # Draw the button rectangle 
        button_rect = pygame.Rect(button_x, button_y, button_width, button_height) 
        # Append button object and piece name to object_list 
        object_list.append((button_rect, piece)) 
        # Draw border behind image 
        pygame.draw.rect(screen, (0,15,15), button_rect) 
        # Draw image in center of button 
        screen.blit(PROMOTION_IMAGES[piece], button_rect.center)

def drawPromotionMenu(player_is_white): 
    
    # Get screen to draw buttons onto 
    screen = pygame.display.set_mode((1000, 900)) 

    # Load images
    loadImages()

    # Stores button tuples for the main three buttons 
    promotion_buttons = [] 

    # Draw buttons 
    draw_buttons(screen, player_is_white, promotion_buttons, 1000) 

    pygame.display.update() 

    return promotion_buttons 

def handle_click(promotion_buttons): 
    # Loop until confirm is True
    run = True 
    while run:
        # Get all events from the event queue
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Handle the quit event to allow the program to exit
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if the rook button is pressed 
                if promotion_buttons[0][0].collidepoint(event.pos):
                    return promotion_buttons[0][1] 
                # Check if the knight button is pressed 
                if promotion_buttons[1][0].collidepoint(event.pos): 
                    return promotion_buttons[0][1]
                # Check if the bishop button is pressed 
                if promotion_buttons[2][0].collidepoint(event.pos): 
                    return promotion_buttons[2][1]
                # Check if the queen button is pressed 
                if promotion_buttons[3][0].collidepoint(event.pos): 
                    return promotion_buttons[3][1]
                
