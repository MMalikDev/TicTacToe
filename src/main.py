import sys

from tqdm import tqdm

import game
import player
from lib.utilities import load_bool, load_variable, logger


def compare_computers(iterations: int) -> None:
    winners = {game.Letter.O: 0, game.Letter.X: 0, None: 0}
    for _ in tqdm(range(iterations)):
        player_X = player.agent.RandomPlayer(game.Letter.X)
        player_O = player.agent.MinimaxPlayer(game.Letter.O)
        result = game.TicTacToe().play(player_X, player_O)
        winners[result] += 1

    message = f"\nAfter {iterations} iterations:\n"
    message += f"\nTotal ties: {winners[None]}\n"
    message += f"\nPlayer X (Random) won {winners[game.Letter.X]} times"
    message += f"\nPlayer O (Minimax) won {winners[game.Letter.O]} times"
    logger.info(message)


def get_opponent() -> game.Player:
    opponent = None
    human = player.human
    machine = player.agent
    message = "Playing %s"

    match (sys.argv):
        case [*_, "cli", "human"]:
            opponent, content = human.PlayerCLI(game.Letter.O), "Human in CLI"
        case [*_, "gui", "human"]:
            opponent, content = human.PlayerGUI(game.Letter.O), "Human in GUI"
        case [*_, "soi", "human"]:
            opponent, content = human.PlayerSOI(game.Letter.O), "Human in SOI"

        case [*_, "random"]:
            opponent, content = machine.RandomPlayer(game.Letter.O), "Random"
        case [*_, "minimax"]:
            opponent, content = machine.MinimaxPlayer(game.Letter.O), "Minimax"

    if not opponent:
        logger.debug("Using env to get opponent")
        match load_variable("OPPONENT", "").lower():
            case "random":
                opponent, content = machine.RandomPlayer(game.Letter.O), "Random"
            case "minimax":
                opponent, content = machine.MinimaxPlayer(game.Letter.O), "Minimax"
            case _:
                opponent, content = machine.MinimaxPlayer(game.Letter.O), "Default"

    logger.info(message, content)
    return opponent


# ---------------------------------------------------------------------- #
# Main Functions                                                         #
# ---------------------------------------------------------------------- #
def main():
    CLI = load_bool("CLI") or load_bool("cli")
    GUI = load_bool("GUI") or load_bool("gui")
    SOI = load_bool("SOI") or load_bool("soi")
    COMPARE = load_bool("COMPARE") or load_bool("compare")
    ITERATIONS = int(load_variable("ITERATIONS", 100))

    if COMPARE:
        compare_computers(ITERATIONS)

    if CLI:
        human = player.human.PlayerCLI(game.Letter.X)
        game.TicTacToeCLI().play(human, get_opponent())
        return

    if GUI:
        human = player.human.PlayerGUI(game.Letter.X)
        game.TicTacToeGUI().play(human, get_opponent())
        return

    if SOI:
        human = player.human.PlayerSOI(game.Letter.X)
        game.TicTacToeSOI().play(human, get_opponent())
        return


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logger.info("You left the game...\n")
