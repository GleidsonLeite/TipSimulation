from src.exception import AppException
from src.entities.AvailableValues import TipValue
from src.entities.Day import Day
from src.entities.Wallet import Wallet
from src.repositories.TipsRepository import TipsRepository
from src.services.BetService import BetService

import random

number_days = 15
number_of_tips_per_day = 105

tips_repository = TipsRepository()
wallet = Wallet(200)

tip_value = TipValue()
tip_values = iter(tip_value)
current_tip_value = next(tip_values)
print(current_tip_value)
for day in range(number_days):
    number_of_reds = 0
    tips_result = [i < 5 for i in range(number_of_tips_per_day)]
    random.shuffle(tips_result)
    for tip_result_was_red in tips_result:
        bet_service = BetService(tips_repository=tips_repository, wallet=wallet)

        current_day = Day(day)
        tip = bet_service.execute(
            day=current_day, value=current_tip_value, is_a_red=tip_result_was_red
        )
        if tip_result_was_red:
            current_tip_value = next(tip_values)
print(wallet.amount)
