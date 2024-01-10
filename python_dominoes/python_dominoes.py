import random


def generate_dominoes() -> list[list[int]]:
    domino_max_range = 7
    completed = []
    dominoes = []

    for i in range(domino_max_range):
        if i != 0:
            completed.append(i - 1)
        for j in range(domino_max_range):
            if j not in completed:
                dominoes.append([i, j])

    return dominoes


def shuffle_dominoes(dominoes: list[list[int]]) -> None:
    random.shuffle(dominoes)


def split_dominoes(dominoes: list[list[int]], start: int, end: int) -> list[list[int]]:
    return dominoes[start:end]


def find_highest_domino(dominoes: list[list[int]]) -> list[int]:
    highest_domino = [-1, -1]

    for i, domino in enumerate(dominoes):
        if domino[0] != domino[1]:
            continue

        if domino > highest_domino:
            highest_domino = domino

    return highest_domino


def get_highest_dominoes_indexes(player: list[list[int]], computer: list[list[int]]):
    while True:
        player_domino = find_highest_domino(player)
        computer_domino = find_highest_domino(computer)

        if player_domino is None and computer_domino is None:
            print("Shuffling")
            shuffle_dominoes(dominoes_list)
            continue

        break

    return player_domino, computer_domino


def get_starting_piece(
    player: list[list[int]], computer: list[list[int]]
) -> tuple[list, str]:
    player_domino, computer_domino = get_highest_dominoes_indexes(player, computer)

    if player_domino > computer_domino:
        domino_snake = player_domino
        player.remove(player_domino)
        status = "computer"
    else:
        computer.remove(computer_domino)
        domino_snake = computer_domino
        status = "player"

    return [domino_snake], status
