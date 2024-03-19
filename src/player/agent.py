import math
import random

import game


class RandomPlayer(game.Player):
    def __init__(self, letter: game.Letter) -> None:
        super().__init__(letter)

    def get_move(self, game: game.TicTacToe) -> int:
        return random.choice(game.available_moves())


class MinimaxPlayer(game.Player):
    def __init__(self, letter: game.Letter) -> None:
        super().__init__(letter)

    def get_move(self, game: game.TicTacToe) -> int:
        if len(game.available_moves()) == 9:
            return random.choice(game.available_moves())

        # Use the minimax algorithm
        return self._minimax(game, self.letter)["position"]

    def _minimax(self, state: game.TicTacToe, player: game.Player):
        current_player = self.letter
        other_player = game.Letter.O if player == game.Letter.X else game.Letter.X

        if state.current_winner == other_player:
            empty_squares = state.count_empty_squares()
            score = int(
                (
                    1 * (empty_squares + 1)
                    if current_player == other_player
                    else -1 * (empty_squares + 1)
                ),
            )
            return {"position": None, "score": score}
        elif not state.empty_squares():
            return {"position": None, "score": 0}

        # Initialise dictionary
        if player == current_player:
            best = {"position": None, "score": -math.inf}
        else:
            best = {"position": None, "score": math.inf}

        for possible_move in state.available_moves():
            # Step 1: Make move and try that spot
            state.made_move(possible_move, player)

            # Step 2: Recurse using minimax to simulate a game after that move
            sim_score = self._minimax(state, other_player)

            # Step 3: Undo the move
            state.board[possible_move] = game.Square.Empty
            sim_score["position"] = possible_move
            state.current_winner = None

            # Step 4: Update dictionaries if needed
            if player == current_player:
                # Maximize the current_player
                if sim_score["score"] > best["score"]:
                    best = sim_score
            else:
                # Minimize other_player
                if sim_score["score"] < best["score"]:
                    best = sim_score

        return best
