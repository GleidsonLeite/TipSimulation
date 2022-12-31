from src.exception import AppException


class Wallet:
    def __init__(self, initial_amount: float) -> None:
        self.__amount = initial_amount

    @property
    def amount(self) -> float:
        return self.__amount

    @amount.setter
    def amount(self, amount: float) -> None:
        if amount < 0:
            raise AppException()
        self.__amount = amount
