from typing import List, Union
from uuid import UUID
from src.entities import Day
from src.entities.Tip import Tip


class TipsRepository:
    def __init__(self) -> None:
        self.__tips: List[Tip] = []

    def create(self, odd: float, value: float) -> Tip:
        created_tip = Tip(odd, value)
        self.__tips.append(created_tip)
        return created_tip

    def add(self, tip: Tip) -> None:
        self.__tips.append(tip)

    def find_by_id(self, id: UUID) -> Union[Tip, None]:
        return next(tip for tip in self.__tips if tip._id == id)

    def find_by_days(self, day: int) -> List[Tip]:
        return [tip for tip in self.__tips if tip.day.day == day]

    def list(self) -> List[Tip]:
        return self.__tips
