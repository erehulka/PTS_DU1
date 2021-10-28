from typing import List
from unittest import TestCase
from simpledominion.BuyDeck import BuyDeckInterface, BuyDeckFactory
from simpledominion.GameCardType import GameCardType, GAME_CARD_TYPE_ESTATE, GAME_CARD_TYPE_COPPER, GAME_CARD_TYPE_FESTIVAL
from test.fake_card import FakeCard


class TestBuyDeck(TestCase):

  def setUp(self):
    buyDeckFactory = BuyDeckFactory()
    self.buydeck = buyDeckFactory.create(GAME_CARD_TYPE_ESTATE, 10)

  def test_add_cards_and_get_size(self):
    self.assertEqual(self.buydeck.isEmpty(), False)
    self.assertEqual(self.buydeck._cardCount, 10)
    card = self.buydeck.getCardInfo()
    self.assertEqual(card, GAME_CARD_TYPE_ESTATE)
    for i in range(10):
      bought = self.buydeck.buy()
    self.assertEqual(bought.cardType, GAME_CARD_TYPE_ESTATE)
    self.assertEqual(self.buydeck.isEmpty(), True)
