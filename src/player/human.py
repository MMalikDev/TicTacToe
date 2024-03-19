import game


class PlayerGUI(game.Player):
    def __init__(self, letter: game.Letter) -> None:
        super().__init__(letter)

    def get_move(self, game: game.TicTacToeGUI) -> int:
        (x, y) = game.get_input()

        number_board = [[i for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
        return number_board[y][x]


class PlayerCLI(game.Player):
    def __init__(self, letter: game.Letter) -> None:
        super().__init__(letter)

    def get_move(self, game: game.TicTacToeCLI) -> int:
        valid_square = False
        while not valid_square:
            try:
                square = input(f"\n{self.letter.value}'s turn. Input move (0-9): ")
                value = int(square) - 1
                if value not in game.available_moves():
                    raise ValueError

                valid_square = True

            except ValueError:
                print("Invalid square. Try again.")

        return value


class PlayerTerm(game.Player):
    def __init__(self, letter: game.Letter) -> None:
        super().__init__(letter)

    def get_move(self, game: game.TicTacToeTerm) -> int:
        valid_square = False
        while not valid_square:
            try:
                square = game.get_input()
                value = int(square) - 1
                if value not in game.available_moves():
                    raise ValueError

                valid_square = True
                game.clear_log()

            except ValueError:
                game.invalid_input()

        return value
