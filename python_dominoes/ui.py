import random
from dominoes import (
    generate_dominoes,
    split_dominoes,
    get_initial_starting_piece,
    shuffle_dominoes,
)  # type: ignore

dominoes_list = generate_dominoes()
shuffle_dominoes(dominoes_list)
computer_pieces = split_dominoes(dominoes_list, 0, 7)
player_pieces = split_dominoes(dominoes_list, 7, 14)
stock_pieces = split_dominoes(dominoes_list, 14, len(dominoes_list))
initial_domino_snake, initial_status = get_initial_starting_piece(
    dominoes_list, player_pieces, computer_pieces
)

snakes = [initial_domino_snake]


def check_winner(pieces: list[list[int]]) -> bool:
    return len(pieces) == 0


def game_over() -> bool:
    if check_winner(player_pieces):
        print(f"Status: The game is over. You won!")
        return True
    if check_winner(computer_pieces):
        print("Status: The game is over. The computer won!")
        return True

    return False


def ui():
    game_player = initial_status
    while True:
        if game_player == "player":
            status = "It's your turn to make a move. Enter your command."
        else:
            status = "Computer is about to make a move. Press Enter to continue..."

        print_stage()
        if game_over():
            break

        print(f"Status: {status}")

        if game_player == "player":
            move = get_input()

            remove_piece(player_pieces, move)
            game_player = "computer"
        else:
            input()
            # all except 0
            comp_options = list(range(-len(computer_pieces), 0)) + list(
                range(1, len(computer_pieces))
            )
            move = random.choice(comp_options)
            remove_piece(computer_pieces, move)

            game_player = "player"


def get_input() -> int:
    while True:
        move = input()

        if not validate_input(move):
            print("Invalid input. Please try again.")
            continue

        return int(move)


def validate_input(move: str) -> bool:
    if move.isalpha():
        return False

    try:
        move = int(move)
    except ValueError:
        return False

    if move < -len(player_pieces) or move > len(player_pieces):
        return False

    return True


def remove_piece(pieces: list[list[int]], move: int):
    if move < 0:
        move = abs(move)
        snake = pieces[move - 1]
        snakes.insert(0, snake)
    elif move == 0:
        remove_stock_piece(pieces)
        return
    else:
        snake = pieces[move - 1]
        snakes.append(snake)

    pieces.remove(snake)


def remove_stock_piece(pieces: list[list[int]]):
    if stock_pieces:
        random_stock: list[int] = random.choice(stock_pieces)
        pieces.append(random_stock)
        stock_pieces.remove(random_stock)


def print_stage() -> None:
    print("=" * 70)
    print("Stock size:", len(stock_pieces))
    print("Computer pieces:", len(computer_pieces))
    print()
    print_snake_pieces()
    print()

    print("Your pieces: ")
    for i, domino in enumerate(player_pieces, start=1):
        print(f"{i}:{domino}")

    print()


def print_snake_pieces():
    if len(snakes) > 6:
        print_snake_pieces_trim()
        return

    for snake in snakes:
        print(snake, end=" ")
    print()


def print_snake_pieces_trim():
    for snake in snakes[:3]:
        print(f"{snake}", end="")
    print("...", end="")
    for snake in snakes[-3::]:
        print(f"{snake}", end="")
    print()
