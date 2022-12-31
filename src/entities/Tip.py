from uuid import uuid4

from src.entities.Day import Day


class Tip:
    def __init__(self, odd: float, value: float, day: Day) -> None:
        self.__odd = odd
        self.__was_green = False
        self.__value = value
        self._id = uuid4()
        self.__day = day

    @property
    def odd(self) -> float:
        return self.__odd

    @property
    def was_green(self) -> bool:
        return self.__was_green

    @was_green.setter
    def was_green(self, was_green: bool) -> None:
        self.__was_green = was_green

    @property
    def value(self) -> float:
        return self.__value

    @property
    def day(self) -> Day:
        return self.__day
