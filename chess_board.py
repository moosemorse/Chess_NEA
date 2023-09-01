import pygame 

pygame.init() 
#display window, set dimensions 800x800 
screen = pygame.display.set_mode([800, 800]) 
#font size variable which we can adjust later 
font_size = 20 
font = pygame.font.SysFont('monospace', font_size) 
#controls the speed at which the game runs at 
timer = pygame.time.Clock() 
fps = 60 

#game variables and images 


#main game loop 
run = True 
while run: 
    timer.tick(fps) 
    #background colour of chess board 
    screen.fill('dark gray') 

    #event handling 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            run = False
    


    pygame.display.flip() 

pygame.quit() 
