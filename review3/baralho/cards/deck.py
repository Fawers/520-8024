import random

from . import card


class Deck:
    def __init__(self):
        self.cards: list[card.Card] = []

    def shuffle(self):
        random.shuffle(self.cards)

    def put(self, card: card.Card):
        self.cards.append(card)

    def take(self) -> card.Card | None:
        try:
            return self.cards.pop()

        except IndexError:
            return None

    def peek(self) -> card.Card | None:
        try:
            return self.cards[-1]

        except IndexError:
            return None

    def get_available_cards(self, c: card.Card) -> list[card.Card]:
        cards: list[card.Card] = []

        for dcard in self.cards:
            if dcard.can_be_placed_onto(c):
                cards.append(dcard)

        return cards

    @classmethod
    def make(cls):
        deck = cls()

        for face in card.Face:
            for nipe in card.Nipe:
                deck.put(card.Card(face, nipe))

        deck.shuffle()
        return deck
