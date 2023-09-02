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

#name of piece accompanied by colour 
#black queen 
b_queen = pygame.image.load('assets/piece/b_queen')
b_queen = pygame.transform.scale(b_queen, (80, 80))
#smaller image for when piece is taken 
b_queen_small = pygame.transform.scale(b_queen, (45, 45))
#black king 
b_king = pygame.image.load('assets/piece/b_king')
b_king = pygame.transform.scale(b_king, (80,80))
b_king_small = pygame.transform.scale(b_king, (45,45))
#black bishop 
b_bishop = pygame.image.load('assets/piece/b_bishop')
b_bishop = pygame.transform.scale(b_bishop, (80, 80))
b_bishop_small = pygame.transform.scale(b_bishop, (45, 45))
#black knight 
b_knight = pygame.image.load('assets/piece/b_knight')
b_knight = pygame.transform.scale(b_knight, (80, 80))
b_knight_small = pygame.transform.scale(b_knight, (45, 45))
#black pawn 
b_pawn = pygame.image.load('assets/piece/b_pawn')
b_pawn = pygame.transform.scale(b_pawn, (80, 80))
b_pawn_small = pygame.transform.scale(b_pawn, (45, 45))
#black rook 
b_rook = pygame.image.load('assets/piece/b_rook')
b_rook = pygame.transform.scale(b_rook, (80, 80))
b_rook_small = pygame.transform.scale(b_rook, (45, 45))
#white bishop 
w_bishop = pygame.image.load('assets/piece/w_bishop')
w_bishop = pygame.transform.scale(w_bishop, (80, 80))
w_bishop_small = pygame.transform.scale(w_bishop, (45, 45))
#white knight 
w_knight = pygame.image.load('assets/piece/w_knight')
w_knight = pygame.transform.scale(w_knight, (80, 80))
w_knight_small = pygame.transform.scale(w_knight, (45, 45))
#white pawn 
w_pawn = pygame.image.load('assets/piece/w_pawn')
w_pawn = pygame.transform.scale(w_pawn, (80, 80))
w_pawn_small = pygame.transform.scale(w_pawn, (45, 45))
#white rook 
w_rook = pygame.image.load('assets/piece/w_rook')
w_rook = pygame.transform.scale(w_rook, (80, 80))
w_rook_small = pygame.transform.scale(w_rook, (45, 45))
#white queen 
w_queen = pygame.image.load('assets/piece/w_queen')
w_queen = pygame.transform.scale(w_queen, (80,80))
w_queen_small = pygame.transform.scale(w_queen, (45,45))
#white king 
w_king = pygame.image.load('assets/piece/w_king')
w_king = pygame.transform.scale(w_king, (80,80))
w_king_small = pygame.transform.scale(w_king, (45,45))

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
