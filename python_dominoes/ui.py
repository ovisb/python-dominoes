from domino import Domino
from domino_handler import DominoHandler


def ui():
    domino_game = Domino()
    domino_handler = DominoHandler(domino_game)

    game_player = domino_game.initial_player_status

    while True:
        status = set_status(game_player)

        print(domino_game)
        if domino_handler.game_over:
            break

        print(f"Status: {status}")

        if game_player == "player":
            domino_handler.player_move()
            game_player = "computer"
        else:
            input()
            domino_handler.computer_move()
            game_player = "player"


def set_status(player: str) -> str:
    if player == "player":
        return "It's your turn to make a move. Enter your command."

    return "Computer is about to make a move. Press Enter to continue..."
