from typing import List
from unittest import TestCase
from simpledominion.game.player.Hand import HandFactory, HandInterface
from simpledominion.game.card.GameCardType import *
from test.fake_card import FakeCard

class FakeDeck:

  _cards: List[FakeCard]

  def __init__(self) -> None:
    self._cards = list()

  def addCard(self, card: FakeCard) -> None:
    self._cards.append(card)

  def shuffleDeck(self) -> None:
    pass

  def draw(self, count: int) -> List[FakeCard]:
    if count > len(self._cards):
      self._cards.extend(self._cards)
    if count > len(self._cards):
      count = len(self._cards)

    to_return = self._cards[:count]
    self._cards = self._cards[count:]
    return to_return

class TestHand(TestCase):

  hand: HandInterface
  deck: FakeDeck

  def assertEmpty(self, hand: HandInterface):
    self.assertEqual(len(hand._cards), 0)

  def setUp(self):
    self.deck = FakeDeck()
    for i in range(7):
      self.deck.addCard(FakeCard(GAME_CARD_TYPE_ESTATE))
    for i in range(3):
      self.deck.addCard(FakeCard(GAME_CARD_TYPE_COPPER))
    handFactory = HandFactory()
    self.hand = handFactory.create(self.deck)

  def test_hand(self):
    # Test that Hand is working correctly, can draw from deck and can play cards
    self.assertEmpty(self.hand)
    self.hand.drawFromDeck(2)
    self.assertEqual(len(self.hand._cards), 2)
    self.assertEqual(self.hand.isActionCard(1), False)
    self.hand.play(1)
    self.assertEqual(len(self.hand._cards), 1)
    self.hand.drawFromDeck(100)
    self.assertEqual(len(self.hand._cards), 17)
    self.hand.drawFromDeck(2)
    self.assertEqual(len(self.hand._cards), 17)
    self.deck.addCard(FakeCard(GAME_CARD_TYPE_COPPER))
    self.hand.drawFromDeck(2)
    self.assertEqual(len(self.hand._cards), 19)
    self.deck.addCard(FakeCard(GAME_CARD_TYPE_COPPER))
    self.hand.drawFromDeck(1)
    self.assertEqual(len(self.hand._cards), 20)
    played = self.hand.discardAllCards()
    self.assertEqual(len(played), 20)
    self.assertEmpty(self.hand)
