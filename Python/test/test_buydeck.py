from typing import List
from unittest import TestCase
from simpledominion.BuyDeck import BuyDeck
from simpledominion.GameCardType import GameCardType, GAME_CARD_TYPE_ESTATE, GAME_CARD_TYPE_COPPER, GAME_CARD_TYPE_FESTIVAL
from test.fake_card import FakeCard


class TestBuyDeck(TestCase):

  def setUp(self):
    self.buydeck = BuyDeck()

  def test_add_cards_and_get_size(self):
    self.assertEqual(self.buydeck.isEmpty(), True)
    self.buydeck.addCard(FakeCard(GAME_CARD_TYPE_ESTATE))
    self.buydeck.addCard(FakeCard(GAME_CARD_TYPE_ESTATE))
    self.buydeck.addCard(FakeCard(GAME_CARD_TYPE_ESTATE))
    self.buydeck.addCard(FakeCard(GAME_CARD_TYPE_ESTATE))
    self.assertEqual(self.buydeck.isEmpty(), False)
    self.buydeck.shuffleDeck()
    self.assertEqual(len(self.buydeck._cards), 4)
    card = self.buydeck.getTopCard()
    self.assertEqual(card.cardType, GAME_CARD_TYPE_ESTATE)
    self.buydeck.shuffleDeck()
    bought = self.buydeck.buy()
    self.assertEqual(bought.cardType, GAME_CARD_TYPE_ESTATE)
    self.assertEqual(len(self.buydeck._cards), 3)
