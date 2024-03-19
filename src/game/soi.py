from .base import Letter, Player, TicTacToe


class TicTacToeSOI(TicTacToe):
    def __init__(self) -> None:
        super().__init__()

    def play(self, X: Player, O: Player) -> None:
        players = {Letter.O: O, Letter.X: X}
        letter = Letter.X

        self.render_board()
        while self.empty_squares():
            square = players[letter].get_move(self)
            if not self.made_move(square, letter):
                continue

            print(f"\n{letter.value} made a move to {square + 1}\n")
            self.render_board()

            if not self.current_winner:
                letter = Letter.O if letter == Letter.X else Letter.X
                continue

            print(f"\nPlayer {letter.value} wins!\n")
            return

        print("\nGame Over! It is a tie.\n")

    def render_board(self) -> None:
        for i in range(3):
            l, r = i * 3, (i + 1) * 3
            row = self.board[l:r]
            nums = [" %i" % (j + 1) for j in range(l, r)]
            for j, square in enumerate(row):
                row[j] = square.value or nums[j]
            print("%s%s%s" % (" | ", " | ".join(row), " | "))
