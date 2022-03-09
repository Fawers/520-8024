import unittest

from cards.card import Card, Face, Nipe


class TestCard(unittest.TestCase):
    def test_cards_of_equal_face_can_be_placed_on_each_other(self):
        c1 = Card(Face.Jack, Nipe.Sword)
        c2 = Card(Face.Jack, Nipe.Heart)

        self.assertTrue(c1.can_be_placed_onto(c2))

    def test_cards_of_equal_nipe_can_be_placed_on_each_other(self):
        c1 = Card(Face.Jack, Nipe.Diamond)
        c2 = Card(Face.Queen, Nipe.Diamond)

        self.assertTrue(c1.can_be_placed_onto(c2))

    def test_cards_of_different_all_cannot_be_placed_on_each_other(self):
        c1 = Card(Face.Ace, Nipe.Sword)
        c2 = Card(Face.King, Nipe.Club)

        self.assertFalse(c1.can_be_placed_onto(c2))
