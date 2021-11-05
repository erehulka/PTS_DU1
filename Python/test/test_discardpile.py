from unittest import TestCase
from simpledominion.game.piles.DiscardPile import DiscardPileFactory
from simpledominion.game.card.GameCardType import GameCardType, GAME_CARD_TYPE_ESTATE, GAME_CARD_TYPE_COPPER
from simpledominion.game.card.CardInterface import CardInterface

class FakeCard(CardInterface):
    def __init__(self, cardType: GameCardType):
        self._cardType = cardType
    @property
    def cardType(self):
    	return self._cardType


class TestDiscardPile(TestCase):
    def assertTopIs(self, pile, string):
        self.assertEqual(pile.getTopCard().cardType.name, string)
        
    def assertTopIsNone(self, pile):
        self.assertIsNone(pile.getTopCard())

    def setUp(self):
        factory = DiscardPileFactory()
        self.pile1 = factory.create([FakeCard(GAME_CARD_TYPE_ESTATE), FakeCard(GAME_CARD_TYPE_COPPER)])
        self.pile2 = factory.create([])
        self.noShufflePile = factory.createNonShuffling([FakeCard(GAME_CARD_TYPE_ESTATE), FakeCard(GAME_CARD_TYPE_COPPER)])
        
    def test_get_top_card(self):
        self.assertTopIs(self.pile1, "Copper")
        
    def test_discard_piles(self):
        self.assertEqual(self.pile2.getSize(), 0)
        self.pile2.addCards([FakeCard(GAME_CARD_TYPE_ESTATE)])
        self.assertEqual(self.pile2.getSize(), 1)
        self.assertTopIs(self.pile2, "Estate")
        self.pile2.addCards([FakeCard(GAME_CARD_TYPE_COPPER)])
        self.assertEqual(self.pile2.getSize(), 2)
        self.assertTopIs(self.pile2, "Copper")

    def test_not_shuffling(self):
        top_card = self.noShufflePile.getTopCard()
        cards = self.noShufflePile.getCards()
        test_card = cards[-1]
        self.assertEqual(top_card, test_card)
        
        
