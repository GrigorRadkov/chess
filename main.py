from cmath import rect
import math as m
from matplotlib.pyplot import bar
import pygame as pg
import engine

WIDTH = HEIGHT = 512
BOARD_DIM = 8
SQ_SIZE = HEIGHT // BOARD_DIM;
MAX_FPS = 60
IMAGES = {}
PIECES = ['wp', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bp', 'bR', 'bN', 'bB', 'bK', 'bQ']

# rgb
white_color = (255, 255, 255)
black_color = (0, 0, 0)
gray_color = (192, 192, 192)

pg.init()

def load_images():
    for piece in PIECES:
        IMAGES[piece] = pg.transform.scale(pg.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))

def main():
    load_images()
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    clock = pg.time.Clock()
    screen.fill(pg.Color(gray_color))
    gameState = engine.GameState()
    sqSelected = () #col, row of selected square
    clickHistory = [] # keeps track only of two subsequent clicks
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                x, y = pg.mouse.get_pos()
                col = x // SQ_SIZE
                row = y // SQ_SIZE
                if sqSelected != (col, row):
                    sqSelected = col, row
                    clickHistory.append(sqSelected)
                else:
                    sqSelected = ()
                    clickHistory = []
                if len(clickHistory) == 2:
                    clickHistory = []
        
                print(sqSelected)
                print(clickHistory)               

                #checkOccupancy(col, row, gameState)

        drawGameState(screen, gameState)
        clock.tick(MAX_FPS)
        pg.display.flip()

def checkOccupancy(x, y, board):
    piece = board[x][y]
    if piece != "--":
        makeMove(piece, board)

def makeMove(piece, board):
    return 0

def drawGameState(screen, gs):
    drawBaseBoard(screen)
    drawPieces(screen, gs.board)

def drawBaseBoard(screen):

    for row in range(BOARD_DIM):
        for col in range(BOARD_DIM):      
            alternate_color = gray_color if((row + col) % 2) else white_color
            pg.draw.rect(screen, alternate_color, pg.Rect((col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE)))

def drawPieces(screen, board):
    for row in range(BOARD_DIM):
        for col in range(BOARD_DIM):
            piece = board[row][col]
            if piece != "--" :
                screen.blit(IMAGES[piece], pg.Rect(col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))

if __name__ == "__main__":
    main()