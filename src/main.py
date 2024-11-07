# HEY! -- Final Project
import pygame, sys
from constants import *

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

screen.fill(BG_COLOR)


def draw_grid():
    # draw horizontal lines
    for i in range(1, BOARD_ROWS):
        pygame.draw.line(
            surface=screen,
            color=LINE_COLOR,
            start_pos=(0, i * SQUARE_SIZE),
            end_pos=(WIDTH, i * SQUARE_SIZE),
            width=LINE_WIDTH,
        )
    # draw vertical lines
    for i in range(1, BOARD_COLS):
        pygame.draw.line(
            surface=screen,
            color=LINE_COLOR,
            start_pos=(i * SQUARE_SIZE, 0),
            end_pos=(i * SQUARE_SIZE, HEIGHT),
            width=LINE_WIDTH,
        )


draw_grid()

while True:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit

    pygame.display.update()
