import pygame 

pygame.init() 

def draw_button(text, x, y): 

    font = pygame.font.Font(None, 32) 

    # Dimensions 
    button_width = 200
    button_height = 30

    button_rect = pygame.Rect(x, y, button_width, button_height) 
    
    # Text drawn onto rectangle 
    text_surface = font.render(text, True, (255, 255, 255)) 

    # Center text 
    text_rect = text_surface.get_rect(topleft = (x + 5, y + 5))
    screen.blit(text_surface, text_rect) 

    return button_rect
    

def draw_heading(screen, text, x, y): 

    font = pygame.font.Font(None, 32) 

    # Render text 
    text_surface = font.render(text, True, (255,255,255)) 

    # Draw text at coordinates x,y 
    text_rect = text_surface.get_rect(topleft = (x, y)) 
    screen.blit(text_surface, text_rect) 


def draw_login_menu(screen): 
    
    clock = pygame.time.Clock() 

    base_font = pygame.font.Font(None, 32) 

    # Text input from user
    username_text = ''
    password_text = ''

    # Initalise all rectangles for each input form 
    username_rect = pygame.Rect(200,300,300,32) 
    password_rect = pygame.Rect(200,400,300,32)
    confirm_rect = draw_button('Confirm details', 200, 500) 
    sign_up_rect = draw_button('Create an account', 200, 550)
    guest_rect = draw_button('Continue as guest', 200, 600)

    # Highlight colours 
    color_active = pygame.Color('White') 
    color_passive = pygame.Color('gray15')
    standard_color = pygame.Color('darkolivegreen') 
    username_color = color_passive 
    password_color = color_passive 

    # Flags to track when boxes are selected 
    username_active = False 
    password_active = False

    run = True 

    while run:  

        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                pygame.quit() 

            # Username box is selected
            if event.type == pygame.MOUSEBUTTONDOWN: 
                if username_rect.collidepoint(event.pos): 
                    username_active = True 
                
                # Username box is de-selected 
                else: 
                    username_active = False 
                
                # Password box is selected
                if password_rect.collidepoint(event.pos): 
                    password_active = True 

                # Pasword box is de-selected
                else: 
                    password_active = False 
                
                if confirm_rect.collidepoint(event.pos): 
                    return username_text, password_text 
                
                if sign_up_rect.collidepoint(event.pos): 
                    return '', '' 
                
                if guest_rect.collidepoint(event.pos): 
                    return None, None 
            
            # User is typing with keyboard 
            if event.type == pygame.KEYDOWN: 
                if username_active == True: 
                    if event.key == pygame.K_BACKSPACE: 
                        username_text = username_text[:-1] 
                    else: 
                        username_text += event.unicode
                
                if password_active == True: 
                    if event.key == pygame.K_BACKSPACE: 
                        password_text = password_text[:-1] 
                    else: 
                        password_text += event.unicode

        # Changing colours of input forms depending on if they have been selected 

        if username_active: 
            username_color = color_active
        else: 
            username_color = color_passive

        if password_active: 
            password_color = color_active
        else: 
            password_color = color_passive 

        # Background colour for menu 

        screen.fill((15,15,15))

        # Heading for title of page 

        draw_heading(screen, 'Login menu', 200, 200) 

        # Headings for each box 

        draw_heading(screen, 'Enter username: ', 200, 260)
        draw_heading(screen, 'Enter password: ', 200, 360)

        # Draw rectangles with colour on border of rectangle
        pygame.draw.rect(screen, username_color, username_rect, 2) 
        pygame.draw.rect(screen, password_color, password_rect, 2)

        # Confirm login details button 
        pygame.draw.rect(screen, standard_color, confirm_rect)
        # Have to recall function so that text is drawn over confirm colour 
        confirm_rect = draw_button('Confirm details', 200, 500)

        # Create account button  
        pygame.draw.rect(screen, standard_color, sign_up_rect)
        # Have to recall function so that text is drawn over confirm colour 
        sign_up_rect = draw_button('Create an account', 200, 550)

        # Continue as guest button 
        pygame.draw.rect(screen, standard_color, guest_rect)
        # Have to recall function so that text is drawn over confirm colour 
        guest_rect = draw_button('Continue as guest', 200, 600)

        # Render text for username and password 
        username_text_surface = base_font.render(username_text, True, (255,255,255)) 
        password_text_surface = base_font.render(password_text, True, (255,255,255)) 

        # Draw the text for username and password, with little offset 
        screen.blit(username_text_surface, (username_rect.x + 5, username_rect.y + 5)) 
        screen.blit(password_text_surface, (password_rect.x + 5, password_rect.y + 5)) 

        # Dynamic width for each form so text doesn't overflow 
        username_rect.w = max(300, username_text_surface.get_width() + 10) 
        password_rect.w = max(300, password_text_surface.get_width() + 10) 

        pygame.display.flip() 
        clock.tick(60)

def draw_create_account_menu(screen): 
    
    clock = pygame.time.Clock() 

    base_font = pygame.font.Font(None, 32) 

    # Text input from user
    username_text = ''
    password_text = ''

    # Initalise all rectangles for each input form 
    username_rect = pygame.Rect(200,300,300,32) 
    password_rect = pygame.Rect(200,400,300,32)
    sign_up_rect = draw_button('Create account', 200, 500)
    login_rect = draw_button('Log into existing', 200, 550) 
    guest_rect = draw_button('Continue as guest', 200, 600)

    # Highlight colours 
    color_active = pygame.Color('White') 
    color_passive = pygame.Color('gray15')
    standard_color = pygame.Color('darkolivegreen') 
    username_color = color_passive 
    password_color = color_passive 

    # Flags to track when boxes are selected 
    username_active = False 
    password_active = False

    run = True 

    while run:  

        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                pygame.quit() 

            # Username box is selected
            if event.type == pygame.MOUSEBUTTONDOWN: 
                if username_rect.collidepoint(event.pos): 
                    username_active = True 
                
                # Username box is de-selected 
                else: 
                    username_active = False 
                
                # Password box is selected
                if password_rect.collidepoint(event.pos): 
                    password_active = True 

                # Pasword box is de-selected
                else: 
                    password_active = False 
                
                if login_rect.collidepoint(event.pos): 
                    return '', ''
                
                if sign_up_rect.collidepoint(event.pos): 
                    return username_text, password_text 
                
                if guest_rect.collidepoint(event.pos): 
                    return None, None 
            
            # User is typing with keyboard 
            if event.type == pygame.KEYDOWN: 
                if username_active == True: 
                    if event.key == pygame.K_BACKSPACE: 
                        username_text = username_text[:-1] 
                    else: 
                        username_text += event.unicode
                
                if password_active == True: 
                    if event.key == pygame.K_BACKSPACE: 
                        password_text = password_text[:-1] 
                    else: 
                        password_text += event.unicode

        # Changing colours of input forms depending on if they have been selected 

        if username_active: 
            username_color = color_active
        else: 
            username_color = color_passive

        if password_active: 
            password_color = color_active
        else: 
            password_color = color_passive 

        # Background colour for menu 

        screen.fill((15,15,15))

        # Heading for title of page 

        draw_heading(screen, 'Creating account', 200, 200) 

        # Headings for each box 

        draw_heading(screen, 'Enter username: ', 200, 260)
        draw_heading(screen, 'Enter password: ', 200, 360)

        # Draw rectangles with colour on border of rectangle
        pygame.draw.rect(screen, username_color, username_rect, 2) 
        pygame.draw.rect(screen, password_color, password_rect, 2)

        # Confirm login details button 
        pygame.draw.rect(screen, standard_color, login_rect)
        # Have to recall function so that text is drawn over confirm colour 
        login_rect = draw_button('Log into existing', 200, 550)

        # Create account button  
        pygame.draw.rect(screen, standard_color, sign_up_rect)
        # Have to recall function so that text is drawn over confirm colour 
        sign_up_rect = draw_button('Create account', 200, 500)

        # Continue as guest button 
        pygame.draw.rect(screen, standard_color, guest_rect)
        # Have to recall function so that text is drawn over confirm colour 
        guest_rect = draw_button('Continue as guest', 200, 600)

        # Render text for username and password 
        username_text_surface = base_font.render(username_text, True, (255,255,255)) 
        password_text_surface = base_font.render(password_text, True, (255,255,255)) 

        # Draw the text for username and password, with little offset 
        screen.blit(username_text_surface, (username_rect.x + 5, username_rect.y + 5)) 
        screen.blit(password_text_surface, (password_rect.x + 5, password_rect.y + 5)) 

        # Dynamic width for each form so text doesn't overflow 
        username_rect.w = max(300, username_text_surface.get_width() + 10) 
        password_rect.w = max(300, password_text_surface.get_width() + 10) 

        pygame.display.flip() 
        clock.tick(60)


if __name__ == '__main__': 
    screen = pygame.display.set_mode((1000, 900)) 
    username, password = draw_login_menu(screen)
    
    if username == None: 
        print("You have chosen to continue as guest") 
    elif username == '': 
        print("You have chosen to create an account") 
    else: 
        print("You are now logged in!")

    username, password = draw_create_account_menu(screen) 


