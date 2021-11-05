from typing import List
from unittest import TestCase
from simpledominion.game.card.GameCard import GameCard
from simpledominion.game.card.GameCardType import *

class MockTurnStatus:

  actions: int = 0
  buys: int = 0
  coins: int = 0

class TestGameCard(TestCase):

  def setUp(self):
    self.estateCard = GameCard(GAME_CARD_TYPE_ESTATE)
    self.copperCard = GameCard(GAME_CARD_TYPE_COPPER)
    self.festivalCard = GameCard(GAME_CARD_TYPE_FESTIVAL)

  def test_evaluate_cards(self):
    status = MockTurnStatus()
    self.copperCard.evaluate(status)
    self.assertEqual(status.coins, 1)
    self.assertEqual(status.buys, 0)
