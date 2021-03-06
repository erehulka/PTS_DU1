from unittest import TestCase
from simpledominion.game.TurnStatus import TurnStatus
from simpledominion.game.piles.BuyDeck import BuyDeckFactory
from simpledominion.game.Turn import TurnFactory, TurnInterface
from simpledominion.game.card.GameCardType import *
from simpledominion.game.card.GameCard import GameCardFactory


class TestTurn(TestCase):

  turn: TurnInterface

  def setUp(self):
    turnFactory = TurnFactory()
    self.turn = turnFactory.create(TurnStatus(1, 0, 0))

  def test_play_turn(self):
    # Test all parts of Turn (Play, Hand etc.)
    # Also test TurnStatus and Card evaluation
    buyDeckFactory = BuyDeckFactory()
    self.turn.addBuyDeck(buyDeckFactory.create(GAME_CARD_TYPE_ESTATE, 10))
    self.assertEqual(len(self.turn.buyDecks), 1)
    self.assertEqual(self.turn.buyCard(0), False)
    self.turn.turnStatus.buys = 10
    self.turn.turnStatus.coins = 10
    self.assertEqual(self.turn.buyCard(0), True)
    self.assertEqual(self.turn.buyCard(100), False)
    self.assertEqual(self.turn.buyCard(0), True)
    cardFactory = GameCardFactory()
    self.turn.hand._cards.append(cardFactory.create(GAME_CARD_TYPE_COPPER))
    self.turn.turnStatus.coins = 0
    self.turn.playCardFromHand(0)
    self.assertEqual(len(self.turn._play._cards), 1)
    self.assertEqual(self.turn.turnStatus.coins, 1)
    self.turn.endTurn()
    # Test that after end of turn, the turnStatus will reset
    self.assertEqual(len(self.turn._play._cards), 0)
    self.assertEqual(len(self.turn.hand._cards), 3)
    for i in range(3):
      self.turn.deck.addCard(cardFactory.create(GAME_CARD_TYPE_ESTATE))
    for i in range(7):
      self.turn.deck.addCard(cardFactory.create(GAME_CARD_TYPE_COPPER))
    self.turn.throwPlayAndHandCardsToDiscardPile()
    self.assertEqual(len(self.turn.hand._cards), 0)
    self.turn.endTurn()
    self.assertEqual(len(self.turn._play._cards), 0)
    self.assertEqual(len(self.turn.hand._cards), 5)
