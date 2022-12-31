class TipValue:
    def __init__(self) -> None:
        self.__available_values = [2, 6, 16]
        self.__id = 0

    def __iter__(self):
        return self

    def __next__(self):
        value = self.__available_values[self.__id]
        next_index = self.__id + 1
        self.__id = next_index if next_index < len(self.__available_values) else 0

        return value
