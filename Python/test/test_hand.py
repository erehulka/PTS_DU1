from typing import List
from unittest import TestCase
from simpledominion.Hand import Hand
from simpledominion.GameCardType import GameCardType, GAME_CARD_TYPE_ESTATE, GAME_CARD_TYPE_COPPER, GAME_CARD_TYPE_FESTIVAL
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

  def assertEmpty(self, hand: Hand):
    self.assertEqual(len(hand._cards), 0)

  def setUp(self):
    self.deck = FakeDeck()
    for i in range(7):
      self.deck.addCard(FakeCard(GAME_CARD_TYPE_ESTATE))
    for i in range(3):
      self.deck.addCard(FakeCard(GAME_CARD_TYPE_COPPER))
    self.hand = Hand(self.deck)

  def test_hand(self):
    pass
