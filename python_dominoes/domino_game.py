from domino import Domino
import random


class DominoGame:
    """
    A class for creating a domino game

    Generates 28 distinct domino pieces

    Responsible for splitting dominoes between user, computer and remaining stock
    """

    def __init__(self, max_range: int = 7) -> None:
        self.__max_range = max_range
        self.__dominoes: list[Domino] = []
        self.__setup()

    def __setup(self):
        self.__generate_dominoes()
        self.__shuffle_dominoes()
        self.__player_dominoes = self.__split_dominoes(0, 7)
        self.__computer_dominoes = self.__split_dominoes(7, 14)
        self.__stock_dominoes = self.__split_dominoes(14, len(self.__dominoes))
        (
            self.__initial_domino_snake,
            self.__initial_status,
        ) = self.__get_initial_starting_piece()
        self.__snakes = [self.__initial_domino_snake]

    @property
    def player_dominoes(self) -> list["Domino"]:
        return self.__player_dominoes

    @property
    def computer_dominoes(self) -> list["Domino"]:
        return self.__computer_dominoes

    @property
    def stock_dominoes(self) -> list["Domino"]:
        return self.__stock_dominoes

    @property
    def dominoes(self) -> list["Domino"]:
        return self.__dominoes

    @property
    def initial_player_status(self) -> str:
        return self.__initial_status

    @property
    def snakes(self) -> list["Domino"]:
        return self.__snakes

    def __generate_dominoes(self) -> None:
        """
        Generates 28 distinct pairs of dominoes
        """
        completed = []

        for i in range(self.__max_range):
            if i != 0:
                completed.append(i - 1)
            for j in range(self.__max_range):
                if j not in completed:
                    self.__dominoes.append(Domino(i, j))

    def __shuffle_dominoes(self) -> None:
        random.shuffle(self.__dominoes)

    def __split_dominoes(self, start: int, end: int) -> list["Domino"]:
        return self.__dominoes[start:end]

    @staticmethod
    def __find_highest_domino(dominoes: list["Domino"]) -> "Domino":
        highest_domino = Domino(-1, -1)

        for i, domino in enumerate(dominoes):
            if domino.piece[0] != domino.piece[1]:
                continue

            if domino > highest_domino:
                highest_domino = domino

        return highest_domino

    def __get_highest_player_comp(self) -> tuple["Domino", "Domino"]:
        while True:
            player_domino = self.__find_highest_domino(self.__player_dominoes)
            computer_domino = self.__find_highest_domino(self.__computer_dominoes)

            if player_domino is None and computer_domino is None:
                print("Shuffling")
                self.__shuffle_dominoes()
                continue

            break

        return player_domino, computer_domino

    def __get_initial_starting_piece(self) -> tuple["Domino", str]:
        player_domino, computer_domino = self.__get_highest_player_comp()

        if player_domino > computer_domino:
            domino_snake = player_domino
            self.__player_dominoes.remove(player_domino)
            status = "computer"
        else:
            self.__computer_dominoes.remove(computer_domino)
            domino_snake = computer_domino
            status = "player"

        return domino_snake, status

    def __str__(self) -> str:
        return f"""
{"=" * 70}
Stock size: {len(self.stock_dominoes)}
Computer pieces: {len(self.computer_dominoes)}

{self.__print_snake_pieces()}

Your pieces: 
{self.__get_player_dominoes()}

        """

    def __print_snake_pieces(self) -> str:
        if len(self.snakes) > 6:
            return self.__print_snake_pieces_trim()

        out = ""
        for snake in self.snakes:
            out += f"{snake} "
        return out

    def __print_snake_pieces_trim(self) -> str:
        out = ""
        for snake in self.snakes[:3]:
            out += f"{snake} "

        out += "..."
        for snake in self.snakes[-3::]:
            out += f"{snake} "
        return out

    def __get_player_dominoes(self) -> str:
        output = []

        for i, domino in enumerate(self.player_dominoes, start=1):
            output.append(f"{i}:{domino}")

        return "\n".join(output)
