import pygame as pg
import engine

WIDTH = HEIGHT = 512
BOARD_DIM = 8
SQ_SIZE = HEIGHT // BOARD_DIM;
MAX_FPS = 60
IMAGES = {}
PIECES = ['wp', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bp', 'bR', 'bN', 'bB', 'bK', 'bQ']

pg.init()

def load_images():
    for piece in PIECES:
        IMAGES[piece] = pg.transform.scale(pg.image.load("images/{piece}.png"), (SQ_SIZE, SQ_SIZE))

def main():
    load_images()
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    clock = pg.time.Clock()
    screen.fill(pg.Color("green"))
    gameState = engine.GameState()
    print(gameState.board)
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        clock.tick(MAX_FPS)
        pg.display.flip()

if __name__ == "__main__":
    main()