from enum import IntEnum as Enum
from dataclasses import dataclass


class Nipe(Enum):
    Sword = 1
    Diamond = 2
    Heart = 3
    Club = 4


class Face(Enum):
    Ace = 1
    Two = 2
    Three = 3
    Four = 4
    Five = 5
    Six = 6
    Seven = 7
    Eight = 8
    Nine = 9
    Ten = 10
    Jack = 11
    Queen = 12
    King = 13


@dataclass(frozen=True)
class Card:
    face: Face
    nipe: Nipe

    def can_be_placed_onto(self, other: 'Card') -> bool:
        return self.nipe == other.nipe or self.face == other.face
