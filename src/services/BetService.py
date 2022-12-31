from random import random
from src.entities.Day import Day
from src.entities.Tip import Tip
from src.entities.Wallet import Wallet
from src.repositories.TipsRepository import TipsRepository


class BetService:
    def __init__(self, wallet: Wallet, tips_repository: TipsRepository) -> None:
        self.__wallet = wallet
        self.__tips_repository = tips_repository

    def execute(self, value: float, day: Day, is_a_red: bool) -> Tip:
        self.__wallet.amount -= value
        tip = Tip(odd=1.05, value=value, day=day)
        tip.was_green = not is_a_red
        if tip.was_green:
            self.__wallet.amount += tip.odd * tip.value
        self.__tips_repository.add(tip)
        return tip
