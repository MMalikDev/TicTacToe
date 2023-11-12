from .base import Letter, Player, Square, TicTacToe

LINE = " | "
EMPTY = "  "


class TicTacToeCLI(TicTacToe):
    def __init__(self) -> None:
        super().__init__()

    def play(self, X: Player, O: Player) -> None:
        players = {Letter.O: O, Letter.X: X}
        letter = Letter.X

        self.render_board_nums()
        while self.empty_squares():
            square = players[letter].get_move(self)
            if not self.made_move(square, letter):
                continue

            print(f"\n{letter.value} made a move to {square   +1}\n")
            self.render_board()

            if not self.current_winner:
                letter = Letter.O if letter == Letter.X else Letter.X
                continue

            print(f"\nPlayer {letter.value} wins!\n")
            return

        print("\nGame Over! It is a tie.\n")

    def render_board(self) -> None:
        board = [self.board[i * 3 : (i + 1) * 3] for i in range(3)]

        for row in board:
            values = [self._get_value(square) for square in row]
            self._display_grid(values)

    def render_board_nums(self) -> None:
        number_board = [
            [str(i + 1) for i in range(j * 3, (j + 1) * 3)] for j in range(3)
        ]

        for row in number_board:
            self._display_grid(row)

    def _display_grid(self, row) -> None:
        print(f"{LINE}{LINE.join(row)}{LINE}")

    def _get_value(self, square: Square) -> str:
        value = square.value
        return value if value is not None else EMPTY
