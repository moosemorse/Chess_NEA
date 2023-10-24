import pygame

#chessboard determines colour of board 
#surface is where objects are drawn onto 

def draw_board(chessboard, surface, width, height): 
    #importing piece assets 
    #back_rank of whites/blacks pieces and pawns repeat 8 times in the next row 
    backrank = ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook']   
    square_dimensions = (width/8, height/8)
    piece_dimensions  = (width/10, height/10)
    for i in range(0,8): 
        for j in range(0,8): 
                #draws chessboard square and then piece ontop 
                if i%2 == 0: 
                    #import dark chessboard squares
                    square = pygame.image.load(f'assets/chessboard/square_d{chessboard}.png') 
                    #re-size asset
                    square = pygame.transform.scale(square, square_dimensions)
                    #draw asset onto surface 
                    surface.blit(square, (i*square_dimensions[0], (square_dimensions[1])*j))
                else: 
                    #import light chessboard squares 
                    square = pygame.image.load(f'assets/chessboard/square_l{chessboard}.png')
                    #re-size asset 
                    square = pygame.transform.scale(square, square_dimensions)
                    #draw asset onto surface 
                    surface.blit(square, (i*square_dimensions[0], (square_dimensions[1])*j)) 
    pass 

#import all piece assets onto squares on the board  
#piece = pygame.image.load(f'assets/piece/b_{backrank[i]}.png')
#re-size piece asset 
#piece = pygame.transform.scale(piece, piece_dimensions)
#draw piece asset onto surface 
#surface.blit(piece, ((i*square_dimensions[0])+10, j))