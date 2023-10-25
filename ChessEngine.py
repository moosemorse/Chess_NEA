class GameState(): 
    def __init__(self): 
        # Board representation 
        # Caps represent black pieces e.g 'B' is a black bishop 
        # Lower-caps represent white pieces e.g 'p' is a white pawn 
        self.board = [
            ["R", "N", "B", "Q", "K", "B", "N", "R"],
            ["P", "P", "P", "P", "P", "P", "P", "P"], 
            ["-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-"],
            ["p", "p", "p", "p", "p", "p", "p", "p"],
            ["r", "n", "b", "q", "k", "b", "n", "r"]
        ]
        self.whiteToMove = True 
        self.moveLog = [] 