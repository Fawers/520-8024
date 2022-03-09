import unittest

from cards.deck import Deck
from cards.card import Card, Face, Nipe



class TestDeck(unittest.TestCase):
    def test_make_creates_a_52_card_deck(self):
        deck = Deck.make()
        self.assertEqual(len(deck.cards), 52)

    def test_make_creates_different_decks(self):
        d1 = Deck.make()
        d2 = Deck.make()
        self.assertNotEqual(d1.cards, d2.cards)

    def test_shuffle_shuffles_cards(self):
        deck = Deck.make()
        cards = deck.cards[:]
        self.assertEqual(deck.cards, cards)

        deck.shuffle()
        self.assertNotEqual(deck.cards, cards)

    def test_put_puts_card_onto_deck(self):
        card = Card(Face.Ace, Nipe.Sword)
        deck = Deck()
        deck.put(card)

        self.assertEqual(deck.cards[0], card)

    def test_peek_peeks_top_card(self):
        card = Card(Face.Ace, Nipe.Sword)
        deck = Deck()
        deck.put(card)

        self.assertEqual(deck.peek(), card)

    def test_peek_does_not_remove_card(self):
        card = Card(Face.Ace, Nipe.Sword)
        deck = Deck()
        deck.put(card)

        self.assertEqual(deck.peek(), card)
        self.assertEqual(deck.cards[0], card)

    def test_peek_empty_deck_returns_None(self):
        deck = Deck()
        self.assertEqual(deck.peek(), None)

    def test_take_takes_top_card(self):
        card = Card(Face.Ace, Nipe.Sword)
        deck = Deck()
        deck.put(card)

        self.assertEqual(deck.take(), card)

    def test_take_removes_card_from_deck(self):
        card = Card(Face.Ace, Nipe.Sword)
        deck = Deck()
        deck.put(card)

        self.assertEqual(deck.take(), card)
        self.assertEqual(deck.take(), None)

    def test_take_empty_deck_returns_None(self):
        deck = Deck()
        self.assertEqual(deck.take(), None)

    def test_get_available_cards_returns_valid_cards(self):
        deck = Deck.make()
        deck.cards.sort(key=lambda card: (card.face, card.nipe))

        card = deck.take()

        if card is None:
            return

        self.assertEqual(card, Card(Face.King, Nipe.Club))

        deck.cards = deck.cards[:12]
        deck.put(Card(Face.King, Nipe.Diamond))
        available_cards = deck.get_available_cards(card)
        valid_cards = [
            Card(Face.Ace, Nipe.Club),
            Card(Face.Two, Nipe.Club),
            Card(Face.Three, Nipe.Club),
            Card(Face.King, Nipe.Diamond)]

        self.assertEqual(available_cards, valid_cards)

