class Domino:
    """
    A class representing a Domino piece
    """

    def __init__(self, first_number: int, second_number: int) -> None:
        self.__first_number = first_number
        self.__second_number = second_number

    @property
    def piece(self) -> list[int]:
        return [self.__first_number, self.__second_number]

    def swap(self) -> None:
        temp = self.__first_number
        self.__first_number = self.__second_number
        self.__second_number = temp

    def __gt__(self, other_object: "Domino") -> bool:
        return self.piece > other_object.piece

    def __eq__(self, other_object: "Domino") -> bool:
        return self.piece == other_object.piece

    def __str__(self) -> str:
        return str(self.piece)

    def __repr__(self) -> str:
        return f"Domino(first_number={self.__first_number}, second_number={self.__second_number})"
