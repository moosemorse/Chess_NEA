import pygame

def draw_conditions_menu(screen, width, height):
    # Set dark background
    screen.fill((15, 15, 15)) 

    # Set up the font for the button text
    font = pygame.font.Font(None, 24)

    # Create buttons for time constraints
    time_buttons = []
    # Time options
    times = ['1', '5', '10', '15', 'Unlimited']  

    # Define button properties
    button_width = 150
    button_height = 50
    margin = 40

    # Calculate positions for buttons
    spacing_x = width // (len(times) + 1)

    for i, text in enumerate(times):
        # Calculate x position for each button
        x = spacing_x * (i + 1) - button_width // 2
        # Center vertically 
        y = width // 2 - button_height // 2 
        button_rect = pygame.Rect(x, y, button_width, button_height)
        time_buttons.append((button_rect, text))
        # Draw button rectangle
        pygame.draw.rect(screen, (100, 100, 100), button_rect)
        # Text drawn onto rectangle 
        text_surface = font.render(text, True, (255, 255, 255)) 
        # Center text 
        text_rect = text_surface.get_rect(center = button_rect.center)
        screen.blit(text_surface, text_rect)

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