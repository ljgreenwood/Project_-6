import pygame, sys
from constants import *

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

#To draw X and O
chip_font = pygame.font.Font(None, CHIP_FONT)

def draw_grid():
    #draw horizontal lines
    for i in range(1, BOARD_ROWS):
        pygame.draw.line(
            screen,
            LINE_COLOR,
            (0, i * SQUARE_SIZE),
            (WIDTH, i * SQUARE_SIZE),
            LINE_WIDTH
        )
    #draw vertical lines
    for i in range(1, BOARD_COLS):
        pygame.draw.line(
            screen,
            LINE_COLOR,
            (i * SQUARE_SIZE, 0),
            (i * SQUARE_SIZE, HEIGHT),
            LINE_WIDTH
        )

def draw_chips():
    chip_x_surf = chip_font.render("x", 0, CROSS_COLOR)
    chip_x_rect = chip_x_surf.get_rect(center=(300,300))
    screen.blit(chip_x_surf, chip_x_rect)

    chip_o_surf = chip_font.render("o", 0, CIRCLE_COLOR)
    chip_o_rect = chip_o_surf.get_rect(center=(500, 300))
    screen.blit(chip_o_surf, chip_o_rect)

screen.fill(BG_COLOR)
draw_grid()
draw_chips()

while True:
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()




