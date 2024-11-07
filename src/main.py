# HEY! -- Final Project
import pygame, sys, tictactoe
from constants import *

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

screen.fill(BG_COLOR)
chip_font = pygame.font.Font(None, CHIP_FONT)

board = tictactoe.initialize_board()
board[1][1] = "x"
board[1][0] = "o"


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


def draw_chips():
    chip_x_surf = chip_font.render("x", 0, CROSS_COLOR)
    chip_o_surf = chip_font.render("o", 0, CIRCLE_COLOR)

    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == "x":
                chip_x_rect = chip_x_surf.get_rect(
                    center=(
                        SQUARE_SIZE * col + SQUARE_SIZE / 2,
                        SQUARE_SIZE * row + SQUARE_SIZE / 2,
                    )
                )
                screen.blit(chip_x_surf, chip_x_rect)
            elif board[row][col] == "o":
                chip_o_rect = chip_o_surf.get_rect(
                    center=(
                        SQUARE_SIZE * col + SQUARE_SIZE / 2,
                        SQUARE_SIZE * row + SQUARE_SIZE / 2,
                    )
                )
                screen.blit(chip_o_surf, chip_o_rect)


def main():
    draw_grid()
    draw_chips()
    while True:
        # event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos  # tuple of coordinates
                print(x, y)
                row, col = (x // 200, y // 200)
                print(row, col)

        pygame.display.update()


if __name__ == "__main__":
    main()
