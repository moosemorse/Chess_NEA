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

#importing piece assets 
#back_rank of whites/blacks pieces and pawns repeat 8 times in the next row 
back_rank = ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook']

#takes in pieces (which actually can be a local variable) 
#chessboard determines colour of board 
#surface is where objects are drawn onto 
def draw_board(pieces,chessboard, surface): 
    for i in range(0,8): 
        if i%2 == 0: 
            square = pygame.image.load(f'assets/chessboard/square_d{chessboard}.png') 
            square = pygame.transform.scale(square, (100,100))
            surface.blit(square, (i*100, 0))
        else: 
            square = pygame.image.load(f'assets/chessboard/square_l{chessboard}.png')
            square = pygame.transform.scale(square, (100,100))
            surface.blit(square, (i*100, 0)) 
        piece = pygame.image.load(f'assets/piece/b_{pieces[i]}.png')
        piece = pygame.transform.scale(piece, (80,80))
        surface.blit(piece, ((i*100)+10, 0))
    pass 

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

    draw_board(back_rank, 'g', screen)

    pygame.display.flip() 

pygame.quit() 
