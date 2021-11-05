from typing import Callable
from unittest import TestCase
from simpledominion.game.GameFactory import GameFactory

class TestGame(TestCase):

  def setUp(self):
    gameFactory = GameFactory()
    self.game = gameFactory.createClassicGame()
    self.game.printWarnings = False

  def assertException(self, f: Callable, *arg, **kwarg) -> None:
    try:
      f(*arg, **kwarg)
      self.assertEqual(True, False)
    except:
      pass

  """ 
  Only way to test Game with deterministic tests - test end of turn, end of game and points.
  All parts of Game are tested in other tests.
  """

  def test_whole_game(self):
    self.game.calculatePoints()
    self.assertEqual(self.game.points, 3)
    self.assertEqual(self.game.playCard(0), True)
    self.assertEqual(self.game.endTurn(), False)
    self.assertEqual(self.game.endPlayCardPhase(), True)
    self.assertEqual(self.game.isEndOfGame(), False)
    self.assertEqual(self.game.endTurn(), True)
    self.assertEqual(len(self.game.turn.hand._cards),5)
    self.game._gameEnded = True
    self.assertException(self.game.playCard, 0)

    self.game._gameEnded = False
    self.assertEqual(self.game.points, 3)
    for buyDeck in self.game.turn.buyDecks:
      buyDeck._cardCount = 0
    self.game.endTurn()
    self.assertEqual(self.game.endGameStrategy.isGameover(), True)
