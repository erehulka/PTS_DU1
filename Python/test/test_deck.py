from typing import List
from unittest import TestCase
from simpledominion.game.piles.Deck import DeckFactory, DeckInterface
from simpledominion.game.card.GameCardType import *
from simpledominion.game.card.CardInterface import CardInterface
from test.fake_card import FakeCard

class MockDiscardPile:

  def __init__(self) -> None:
    pass

  def getCards(self) -> List[CardInterface]:
    return [FakeCard(GAME_CARD_TYPE_ESTATE), FakeCard(GAME_CARD_TYPE_FESTIVAL), FakeCard(GAME_CARD_TYPE_COPPER)]

class TestDeck(TestCase):

  def assertEmpty(self, deck: DeckInterface):
    self.assertEqual(len(deck._cards), 0)

  def setUp(self):
    deckFactory = DeckFactory()
    self.deck = deckFactory.create(MockDiscardPile())

  def test_add_cards_and_get_size(self):
    self.assertEmpty(self.deck)
    self.deck.addCard(FakeCard(GAME_CARD_TYPE_COPPER))
    self.deck.addCard(FakeCard(GAME_CARD_TYPE_ESTATE))
    self.assertEqual(len(self.deck._cards), 2)
    self.deck.shuffleDeck()
    self.assertEqual(len(self.deck._cards), 2)
    self.deck.addCard(FakeCard(GAME_CARD_TYPE_ESTATE))
    self.deck.addCard(FakeCard(GAME_CARD_TYPE_ESTATE))
    self.deck.addCard(FakeCard(GAME_CARD_TYPE_ESTATE))
    self.deck.addCard(FakeCard(GAME_CARD_TYPE_ESTATE))
    drew = self.deck.draw(4)
    self.assertEqual(len(self.deck._cards), 2)
    top_card = self.deck._cards[0]
    self.assertEqual(len(drew), 4)
    drew = self.deck.draw(4)
    self.assertEqual(drew[0], top_card)
    self.assertEqual(len(self.deck._cards), 1)
    self.assertEqual(len(drew), 4)
