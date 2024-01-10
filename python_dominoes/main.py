"""Main module"""
from python_dominoes import (
    generate_dominoes,
    split_dominoes,
    get_starting_piece,
    shuffle_dominoes,
    get_highest_dominoes_indexes,
)  # type: ignore


def main() -> None:
    """Main function"""
    dominoes_list = generate_dominoes()

    shuffle_dominoes(dominoes_list)

    computer_pieces = split_dominoes(dominoes_list, 0, 7)
    player_pieces = split_dominoes(dominoes_list, 7, 14)
    stock_pieces = split_dominoes(dominoes_list, 14, len(dominoes_list))

    domino_snake, status = get_starting_piece(player_pieces, computer_pieces)

    print("Stock pieces:", stock_pieces)
    print("Computer pieces:", computer_pieces)
    print("Player pieces:", player_pieces)
    print("Domino snake:", domino_snake)
    print("Status:", status)


if __name__ == "__main__":
    main()
