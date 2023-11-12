import sys
from typing import Tuple

import pygame

from lib.utilities import logger

from .base import Letter, Player, TicTacToe

BOARD = pygame.image.load("assets/board.svg")
O_IMAGE = pygame.image.load("assets/o.svg")
X_IMAGE = pygame.image.load("assets/x.svg")
WINNING_IMAGE = {Letter.X: "assets/xWins.svg", Letter.O: "assets/oWins.svg"}


class TicTacToeGUI(TicTacToe):
    def __init__(self, size: int = 900, bg_color: pygame.Color = (0, 0, 0)) -> None:
        super().__init__()
        self.size = size
        self.bg_color = bg_color
        self.cell = self.size // 3

        self.default_graphic = [[[None, None] for _ in range(3)] for _ in range(3)]
        self.graphical_board = self.default_graphic.copy()

        pygame.init()
        pygame.display.set_caption("Tic Tac Toe!")
        self.screen = pygame.display.set_mode((self.size, self.size))

        self._reset_display()

    def play(self, X: Player, O: Player) -> None:
        players = {Letter.O: O, Letter.X: X}
        letter = Letter.X

        self.render_board()
        while self.empty_squares():
            self.display_caption(letter)
            square = players[letter].get_move(self)
            if not self.made_move(square, letter):
                continue

            logger.debug(f"{letter.value} made a move to {square}")
            self.display_caption(letter)
            self.render_board()
            self.update_display()

            if self.winner(square, letter):
                logger.debug(f"Player{letter.value} wins!")
                self.show_winner(square, letter)
                self.new_game()

            if self.no_more_moves():
                logger.debug(f"Game Over! It is a tie.")
                self.new_game()

            letter = Letter.O if letter == Letter.X else Letter.X

    def _quit(self, event) -> None:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    def get_input(self) -> Tuple[int, int]:
        while True:
            for event in pygame.event.get():
                self._quit(event)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    position = pygame.mouse.get_pos()
                    return (position[0] // self.cell, position[1] // self.cell)

    def render_board(self) -> None:
        board = [self.board[i * 3 : (i + 1) * 3] for i in range(3)]
        for i, row in enumerate(board):
            for j, col in enumerate(row):
                if col == Letter.X:
                    self._set_square(i, j, X_IMAGE)
                    continue
                if col == Letter.O:
                    self._set_square(i, j, O_IMAGE)
                    continue

    def _set_square(self, i: int, j: int, img: pygame.surface.Surface) -> None:
        x = (self.cell * j) + (self.cell / 2)
        y = (self.cell * i) + (self.cell / 2)

        self.graphical_board[i][j][0] = img
        self.graphical_board[i][j][1] = img.get_rect(center=(x, y))
        self.screen.blit(self.graphical_board[i][j][0], self.graphical_board[i][j][1])

    def display_caption(self, player: Letter) -> None:
        if player == self.current_winner:
            caption = f"Player {player.value} wins!"
        elif self.no_more_moves():
            caption = "Game Over! It is a tie."
        else:
            caption = f"Player {player.value}'s turn!"

        pygame.display.set_caption(caption)

    def update_display(self) -> None:
        pygame.display.update()

    def _reset_display(self) -> None:
        self.screen.fill(self.bg_color)
        self.screen.blit(BOARD, (0, 0))
        self.update_display()

    def reset(self) -> None:
        self.current_winner = None
        self.board = self.empty_board.copy()
        self.graphical_board = self.default_graphic.copy()

        self._reset_display()

    def new_game(self) -> None:
        while True:
            for event in pygame.event.get():
                self._quit(event)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.reset()
                    return

    def show_winner(self, square, letter) -> None:
        row_idx = square // 3
        row = self.board[row_idx * 3 : (row_idx + 1) * 3]

        column_idx = square % 3
        column = [self.board[column_idx + i * 3] for i in range(3)]

        if all([spot == letter for spot in row]):
            self._set_winning_row(row_idx, letter)
        elif all([spot == letter for spot in column]):
            self._set_winning_colum(column_idx, letter)
        elif square % 2 == 0:
            diagonal_1 = [self.board[i] for i in [0, 4, 8]]
            diagonal_2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal_1]):
                self._set_winning_diagonal1(letter)
            elif all([spot == letter for spot in diagonal_2]):
                self._set_winning_diagonal2(letter)

        self.update_display()

    def _set_winning_row(self, row: int, letter: Letter) -> None:
        for i in range(3):
            self._set_winning_square(row, i, letter)

    def _set_winning_colum(self, col: int, letter: Letter) -> None:
        for i in range(3):
            self._set_winning_square(i, col, letter)

    def _set_winning_diagonal1(self, letter: Letter) -> None:
        self._set_winning_square(0, 0, letter)
        self._set_winning_square(1, 1, letter)
        self._set_winning_square(2, 2, letter)

    def _set_winning_diagonal2(self, letter: Letter) -> None:
        self._set_winning_square(0, 2, letter)
        self._set_winning_square(1, 1, letter)
        self._set_winning_square(2, 0, letter)

    def _set_winning_square(self, x: int, y: int, winner: Letter) -> None:
        image = WINNING_IMAGE[winner]

        self.graphical_board[x][y][0] = pygame.image.load(image)
        self.screen.blit(self.graphical_board[x][y][0], self.graphical_board[x][y][1])
