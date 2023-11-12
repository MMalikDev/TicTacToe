import sys

from tqdm import tqdm

from lib import game, player
from lib.utilities import load_variable, logger


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
    message = "Playing %s"
    opponent = None

    match (sys.argv):
        case [*_, "cli", "human"]:
            opponent, content = player.human.PlayerCLI(game.Letter.O), "Human in CLI"
        case [*_, "gui", "human"]:
            opponent, content = player.human.PlayerGUI(game.Letter.O), "Human in GUI"
        case [*_, "random"]:
            opponent, content = player.agent.RandomPlayer(game.Letter.O), "Random"
        case [*_, "minimax"]:
            opponent, content = player.agent.MinimaxPlayer(game.Letter.O), "Minimax"

    if not opponent:
        logger.debug("Using env to get opponent")
        match load_variable("OPPONENT", "").lower():
            case "random":
                opponent, content = player.agent.RandomPlayer(game.Letter.O), "Random"
            case "minimax":
                opponent, content = player.agent.MinimaxPlayer(game.Letter.O), "Minimax"
            case _:
                opponent, content = player.agent.MinimaxPlayer(game.Letter.O), "Default"

    logger.info(message, content)
    return opponent


# ---------------------------------------------------------------------- #
# Main Functions                                                         #
# ---------------------------------------------------------------------- #
def main():
    COMPARE = load_variable("COMPARE", "").upper() in ["1", "TRUE"]
    GUI = load_variable("GUI", "").upper() in ["1", "TRUE"]
    CLI = load_variable("CLI", "").upper() in ["1", "TRUE"]
    ITERATIONS = int(load_variable("ITERATIONS", 100))

    if COMPARE or "compare" in sys.argv:
        compare_computers(ITERATIONS)

    if GUI or "gui" in sys.argv:
        human = player.human.PlayerGUI(game.Letter.X)
        game.TicTacToeGUI().play(human, get_opponent())
        return

    if CLI or "cli" in sys.argv:
        human = player.human.PlayerCLI(game.Letter.X)
        game.TicTacToeCLI().play(human, get_opponent())
        return


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logger.info("You left the game...\n")