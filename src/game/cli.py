from collections import namedtuple

from blessed import Terminal

from .base import Letter, Player, Square, TicTacToe

Point = namedtuple("Point", "x, y")


class TicTacToeCLI(TicTacToe):
    def __init__(self) -> None:
        super().__init__()
        self.display = Terminal()

        self.color_bg = self.display.on_black
        self.color_grid = self.display.on_gray
        self.color_cell = self.display.white_on_black

        self.boundary = self.color_grid(" ")
        self.exit_msg = self.color_bg(" Press Any Key To Exit...")
        self.invalid = self.color_bg(" Invalid square. Try again.")

        self.init_sizes()

    def init_sizes(self):
        self.blank = self.color_bg(" " * self.display.width)

        w_off = self.display.width // 4
        h_off = self.display.height // 4
        w = self.display.width // 2
        h = self.display.height // 2

        self.horizontal = self.boundary * w
        self.top = Point(h_off + h // 3, w_off)
        self.bottom = Point(h_off + h * 2 // 3, w_off)

        vertical = range(0, h)
        self.left = [Point(w // 3 + w_off, h_off + i) for i in vertical]
        self.left += [Point(w // 3 + 1 + w_off, h_off + i) for i in vertical]
        self.right = [Point(w * 2 // 3 + w_off, h_off + i) for i in vertical]
        self.right += [Point(w * 2 // 3 + 1 + w_off, h_off + i) for i in vertical]

        self.cells = [
            (h_off + h // 6, w_off + w // 6),
            (h_off + h // 6, w_off + w // 2),
            (h_off + h // 6, w_off + w * 5 // 6),
            (h_off + h // 2, w_off + w // 6),
            (h_off + h // 2, w_off + w // 2),
            (h_off + h // 2, w_off + w * 5 // 6),
            (h_off + h * 5 // 6, w_off + w // 6),
            (h_off + h * 5 // 6, w_off + w // 2),
            (h_off + h * 5 // 6, w_off + w * 5 // 6),
        ]

    def get_input(self):
        with self.display.cbreak():
            return self.display.inkey()

    def play(self, X: Player, O: Player) -> None:
        msg = " Game Over! It is a tie."
        players = {Letter.O: O, Letter.X: X}
        letter = Letter.X

        self.clear_grid()
        self.render_grid()
        self.render_board()
        while self.empty_squares():
            self.show_current_player(letter)

            square = players[letter].get_move(self)
            if not self.made_move(square, letter):
                continue

            self.render_board()
            if not self.current_winner:
                letter = Letter.O if letter == Letter.X else Letter.X
                continue

            msg = f" Player {letter.value} wins!"
            break

        self.game_over_msg(msg)
        self.exit()

    def game_over_msg(self, msg: str) -> None:
        with self.display.location(), self.display.cbreak():
            print(self.display.move_yx(1, 0), self.color_bg(msg))
            print(self.display.move_yx(2, 0), self.exit_msg)
            self.display.inkey()

    def show_current_player(self, letter: Letter) -> None:
        msg = f" Player {letter.value}'s turn..."
        with self.display.location():
            print(self.display.move_yx(1, 0), self.color_bg(msg))

    def invalid_input(self) -> None:
        with self.display.location():
            print(self.display.move_yx(2, 0), self.invalid)

    def clear_log(self) -> None:
        with self.display.location():
            print(self.display.move_yx(1, 0), self.blank)
            print(self.display.move_yx(2, 0), self.blank)

    def render_board(self) -> None:
        for i, square in enumerate(self.board):
            self.display_cell(i, square)

    def render_grid(self) -> None:
        with self.display.location():
            print(self.display.move_yx(self.top.x, self.top.y) + self.horizontal)
            for pt in self.left:
                print(self.display.move_yx(pt.y, pt.x) + self.boundary)
            for pt in self.right:
                print(self.display.move_yx(pt.y, pt.x) + self.boundary)
            print(self.display.move_yx(self.bottom.x, self.bottom.y) + self.horizontal)

    def display_cell(self, idx: int, square: Square) -> None:
        x, y = self.cells[idx]
        value = square.value if square.value else str(idx + 1)
        with self.display.location():
            print(self.display.move_yx(x, y) + (self.color_cell(value)))

    def clear_grid(self) -> None:
        print(self.color_bg(self.display.clear))

    def exit(self) -> None:
        print(self.display.normal)
        print(self.display.clear)
