from abc import ABC, abstractmethod
from enum import Enum
from typing import List, Optional


class Letter(Enum):
    X = "\u274C"
    O = "\u2B55"


class Square(Enum):
    Empty = None
    X = Letter.X
    O = Letter.O


class Player(ABC):
    def __init__(self, letter: Letter) -> None:
        self.letter = letter

    @abstractmethod
    def get_move(self, game: "TicTacToe") -> int: ...


class TicTacToe:
    def __init__(self) -> None:
        # Generate a one Dimensional list to represent a 3x3 board
        self.empty_board = [Square.Empty for _ in range(9)]
        self.board: List[Square] = self.empty_board.copy()
        self.current_winner: Optional[Letter] = None

    def play(self, X: Player, O: Player) -> Optional[Letter]:
        players = {Letter.O: O, Letter.X: X}
        letter = Letter.X

        while self.empty_squares():
            square = players[letter].get_move(self)
            if not self.made_move(square, letter):
                continue

            if not self.current_winner:
                letter = Letter.O if letter == Letter.X else Letter.X
                continue

            return letter

    def empty_squares(self) -> bool:
        return Square.Empty in self.board

    def count_empty_squares(self) -> int:
        return self.board.count(Square.Empty)

    def available_moves(self) -> List[int]:
        return [i for i, spot in enumerate(self.board) if spot == Square.Empty]

    def no_more_moves(self) -> bool:
        return len(self.available_moves()) == 0

    def made_move(self, square: int, letter: Letter) -> bool:
        if not self.board[square] == Square.Empty:
            return False

        self.board[square] = letter
        if self.winner(square, letter):
            self.current_winner = letter
        return True

    def winner(self, square: Square, letter: Letter) -> bool:
        return (
            self._check_row(square, letter)
            or self._check_column(square, letter)
            or self._check_diagonal(square, letter)
        )

    def _check_row(self, square: Square, letter: Letter) -> bool:
        row = self.board[square // 3 * 3 : (square // 3 + 1) * 3]
        return all([spot == letter for spot in row])

    def _check_column(self, square: Square, letter: Letter) -> bool:
        column = [self.board[square % 3 + i * 3] for i in range(3)]
        return all([spot == letter for spot in column])

    def _check_diagonal(self, square: Square, letter: Letter) -> bool:
        return square % 2 == 0 and (
            all([spot == letter for spot in [self.board[i] for i in [2, 4, 6]]])
            or all([spot == letter for spot in [self.board[i] for i in [0, 4, 8]]])
        )
