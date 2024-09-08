import pygame
import sys

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800
BOARD_SIZE = 8
SQUARE_SIZE = SCREEN_WIDTH // BOARD_SIZE
WHITE = (240, 217, 181)
BLACK = (181, 136, 99)

# Pieces images
PIECE_IMAGES = {}

# Initialize pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Chess 0.0')


# Load images
def load_images():
    pieces = ['w_pawn', 'w_rook', 'w_knight', 'w_bishop', 'w_queen', 'w_king',
              'b_pawn', 'b_rook', 'b_knight', 'b_bishop', 'b_queen', 'b_king']
    for piece in pieces:
        PIECE_IMAGES[piece] = pygame.transform.scale(pygame.image.load(f'images/{piece}.png'), (SQUARE_SIZE, SQUARE_SIZE))

class Piece:
    def __init__(self, color):
        self.color = color
        self.image = None

    def draw(self, screen, row, col):
        if self.image:
            screen.blit(self.image, (col * SQUARE_SIZE, row * SQUARE_SIZE))

    def get_moves(self, board, row, col):
        # TODO: Implement this method
        pass

class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.image = PIECE_IMAGES[f'{color}_pawn']

    def get_moves(self, board, row, col):
        #TODO
        pass

class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.image = PIECE_IMAGES[f'{color}_rook']

    def get_moves(self, board, row, col):
        #TODO
        pass

class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.image = PIECE_IMAGES[f'{color}_knight']

    def get_moves(self, board, row, col):
        #TODO
        pass

class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.image = PIECE_IMAGES[f'{color}_bishop']

    def get_moves(self, board, row, col):
        #TODO
        pass

class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.image = PIECE_IMAGES[f'{color}_queen']

    def get_moves(self, board, row, col):
        #TODO
        pass

class King(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.image = PIECE_IMAGES[f'{color}_king']

    def get_moves(self, board, row, col):
        #TODO
        pass

class Board:
    def __init__(self):
        self.board = self.create_board()

    def create_board(self):
        # Initialize board with empty squares
        board = [[None for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

        # Placing pawns on the board
        for i in range(BOARD_SIZE):
            board[6][i] = Pawn('w') # White pawns
            board[1][i] = Pawn('b') # Black pawns

        # Placing rooks on the board
        board[7][0] = board[7][7] = Rook('w')
        board[0][0] = board[0][7] = Rook('b')

        # Placing knights on the board
        board[7][1] = board[7][6] = Knight('w')
        board[0][1] = board[0][6] = Knight('b')

        # Placing bishops on the board
        board[7][2] = board[7][5] = Bishop('w')
        board[0][2] = board[0][5] = Bishop('b')

        # Placing queens on the board
        board[7][3] = Queen('w')
        board[0][3] = Queen('b')

        # Placing kings on the board
        board[7][4] = King('w')
        board[0][4] = King('b')

        return board
    
    def draw(self, screen):
            for row in range(BOARD_SIZE):
                for col in range(BOARD_SIZE):
                    color = WHITE if (row + col) % 2 == 0 else BLACK
                    pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                    piece = self.board[row][col]
                    if piece:
                        piece.draw(screen, row, col)

class Game:
    def __init__(self):
        self.board = Board()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.board.draw(screen)
            pygame.display.flip()

if __name__ == '__main__':
    load_images()
    game = Game()
    game.run()
    #
#2
#3
#4
#5
#zzz
#
##
###
####
#####
######
#######
########
#########
##########
###########
