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
    if not stock_pieces:
        print("Status: The game is over. It's a draw!")
        return True
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
            while True:
                move = input()
                if not validate_input(move):
                    print("Invalid input. Please try again.")
                    continue

                move = int(move)

                if not move_domino(player_pieces, move):
                    print("Illegal move. Please try again.")
                    continue

                break

            game_player = "computer"
        else:
            input()
            while True:
                comp_options = list(
                    range(-len(computer_pieces), len(computer_pieces) + 1)
                )
                move = random.choice(comp_options)

                if move_domino(computer_pieces, move):
                    break

            game_player = "player"


def move_domino(pieces: list[list[int]], move: int) -> bool:
    if move == 0 and stock_pieces:
        remove_stock_piece(pieces)
        return True

    if move < 0:
        move = abs(move)
        return move_domino_left(pieces, move)
    else:
        return move_domino_right(pieces, move)


def move_domino_left(pieces: list[list[int]], move: int) -> bool:
    player_domino_piece = pieces[move - 1]
    if not validate_neighbour_domino(player_domino_piece, 0):
        return False

    snake_piece_first_number = snakes[0][0]
    player_domino_piece_second_number = player_domino_piece[1]

    if not swapped(player_domino_piece_second_number, snake_piece_first_number):
        swap_domino_number_pair(player_domino_piece)

    snakes.insert(0, player_domino_piece)
    pieces.remove(player_domino_piece)
    return True


def move_domino_right(pieces: list[list[int]], move: int) -> bool:
    player_domino_piece = pieces[move - 1]
    if not validate_neighbour_domino(player_domino_piece, -1):
        return False

    snake_piece_second_number = snakes[-1][1]
    player_domino_piece_first_number = player_domino_piece[0]

    if not swapped(player_domino_piece_first_number, snake_piece_second_number):
        swap_domino_number_pair(player_domino_piece)

    snakes.append(player_domino_piece)
    pieces.remove(player_domino_piece)
    return True


def swap_domino_number_pair(player_domino_piece: list[int]) -> None:
    temp = player_domino_piece[0]
    player_domino_piece[0] = player_domino_piece[1]
    player_domino_piece[1] = temp


def swapped(
    player_domino_piece_first_number: int, snake_piece_second_number: int
) -> bool:
    return player_domino_piece_first_number == snake_piece_second_number


def validate_neighbour_domino(snake_piece: list[int], index: int) -> bool:
    """
    Validate neighbour domino
    0 checks first pair on the left and -1 checks last pair on the right
    """
    neighbour_snake_pair_number = snakes[index][index]
    return neighbour_snake_pair_number in snake_piece


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


def remove_stock_piece(pieces: list[list[int]]) -> None:
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


def print_snake_pieces() -> None:
    if len(snakes) > 6:
        print_snake_pieces_trim()
        return

    for snake in snakes:
        print(snake, end=" ")
    print()


def print_snake_pieces_trim() -> None:
    for snake in snakes[:3]:
        print(f"{snake}", end="")
    print("...", end="")
    for snake in snakes[-3::]:
        print(f"{snake}", end="")
    print()
