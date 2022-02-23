import abc
from typing import Any


class GameError(Exception, metaclass=abc.ABCMeta):
    __match_args__ = ('value',)

    def __init__(self, value: Any):
        super().__init__(value)
        self.value = value

class InvalidSymbol(GameError):
    pass

class InvalidRowOrColumn(GameError):
    pass

class GridPositionAlreadyFilled(GameError):
    pass
