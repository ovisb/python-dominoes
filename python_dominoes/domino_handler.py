import random

from domino import Domino


class DominoHandler:
    def __init__(self, domino: "Domino"):
        self.__domino = domino

    @property
    def game_over(self) -> bool:
        if not self.__domino.stock_dominoes:
            print("Status: The game is over. It's a draw!")
            return True
        if self.__check_winner(self.__domino.player_dominoes):
            print("Status: The game is over. You won!")
            return True
        if self.__check_winner(self.__domino.computer_dominoes):
            print("Status: The game is over. The computer won!")
            return True

        return False

    @staticmethod
    def __check_winner(pieces: list[list[int]]) -> bool:
        return len(pieces) == 0

    def player_move(self) -> None:
        while True:
            move = input()
            if not self.__validate_player_input(move):
                print("Invalid input. Please try again.")
                continue

            choice = int(move)

            if not self.__move_domino(self.__domino.player_dominoes, choice):
                print("Illegal move. Please try again.")
                continue

            break

    def computer_move(self) -> None:
        score_dict = self.__calculate_domino_weight()
        found = False

        scores_list = sorted(score_dict.keys(), reverse=True)
        for score in scores_list:
            move = score_dict[score]

            lef_and_right = (-move, move)
            for move in lef_and_right:
                if self.__move_domino(self.__domino.computer_dominoes, move):
                    found = True
                    break

            if found:
                break

        if not found:
            self.__move_domino(self.__domino.computer_dominoes, 0)

    def __calculate_domino_weight(self) -> dict[int, int]:
        frequency_occurrence = self.__get_number_frequency()

        total_score_idx = {}
        for idx, domino_pair in enumerate(self.__domino.computer_dominoes):
            total = sum(frequency_occurrence[item] for item in domino_pair)
            total_score_idx[total] = idx

        return total_score_idx

    def __get_number_frequency(self):
        frequency_occurrence = {}

        self.__count_number_frequency(
            frequency_occurrence, self.__domino.computer_dominoes
        )
        self.__count_number_frequency(frequency_occurrence, self.__domino.snakes)

        return frequency_occurrence

    @staticmethod
    def __count_number_frequency(
        frequency_occurrence: dict[int, int], pieces: list[list[int]]
    ) -> None:
        for domino in range(7):
            for domino_pair in pieces:
                frequency_occurrence.setdefault(domino, 0)
                frequency_occurrence[domino] += domino_pair.count(domino)

    def __validate_player_input(self, move: str) -> bool:
        if move.isalpha():
            return False

        try:
            choice = int(move)
        except ValueError:
            return False

        if choice < -len(self.__domino.player_dominoes) or choice > len(
            self.__domino.player_dominoes
        ):
            return False

        return True

    def __move_domino(self, pieces: list[list[int]], move: int) -> bool:
        if move == 0:
            self.__remove_stock_piece(pieces)
            return True

        if move < 0:
            move = abs(move)
            return self.__move_domino_left(pieces, move)
        else:
            return self.__move_domino_right(pieces, move)

    def __remove_stock_piece(self, pieces: list[list[int]]) -> None:
        if self.__domino.stock_dominoes:
            random_stock: list[int] = random.choice(self.__domino.stock_dominoes)
            pieces.append(random_stock)
            self.__domino.stock_dominoes.remove(random_stock)

    def __move_domino_left(self, pieces: list[list[int]], move: int) -> bool:
        played_domino_piece = self.__get_domino_piece(pieces, move)
        if not self.__validate_neighbour_domino(played_domino_piece, 0):
            return False

        snake_piece_first_number = self.__domino.snakes[0][0]
        player_domino_piece_second_number = played_domino_piece[1]

        if not self.__swapped(
            player_domino_piece_second_number, snake_piece_first_number
        ):
            self.__swap_domino_number_pair(played_domino_piece)

        self.__domino.snakes.insert(0, played_domino_piece)
        pieces.remove(played_domino_piece)
        return True

    def __move_domino_right(self, pieces: list[list[int]], move: int) -> bool:
        player_domino_piece = self.__get_domino_piece(pieces, move)
        if not self.__validate_neighbour_domino(player_domino_piece, -1):
            return False

        snake_piece_second_number = self.__domino.snakes[-1][1]
        player_domino_piece_first_number = player_domino_piece[0]

        if not self.__swapped(
            player_domino_piece_first_number, snake_piece_second_number
        ):
            self.__swap_domino_number_pair(player_domino_piece)

        self.__domino.snakes.append(player_domino_piece)
        pieces.remove(player_domino_piece)
        return True

    @staticmethod
    def __get_domino_piece(pieces: list[list[int]], move: int) -> list[int]:
        return pieces[move - 1]

    def __validate_neighbour_domino(self, snake_piece: list[int], index: int) -> bool:
        """
        Validate neighbour domino
        0 checks first pair on the left and -1 checks last pair on the right
        """
        neighbour_snake_pair_number = self.__domino.snakes[index][index]
        return neighbour_snake_pair_number in snake_piece

    @staticmethod
    def __swapped(
        player_domino_piece_first_number: int, snake_piece_second_number: int
    ) -> bool:
        return player_domino_piece_first_number == snake_piece_second_number

    @staticmethod
    def __swap_domino_number_pair(player_domino_piece: list[int]) -> None:
        temp = player_domino_piece[0]
        player_domino_piece[0] = player_domino_piece[1]
        player_domino_piece[1] = temp
