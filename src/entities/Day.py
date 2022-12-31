class Day:
    def __init__(self, day: int) -> None:
        self.__day = day

    @property
    def day(self) -> int:
        return self.__day
