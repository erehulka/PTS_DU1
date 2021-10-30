from unittest import TestCase
from simpledominion.GameFactory import GameFactory

class TestGame(TestCase):

  def setUp(self):
    gameFactory = GameFactory()
    self.game = gameFactory.createClassicGame()

  def test_whole_game(self):
    self.game.calculatePoints()
    self.assertEqual(self.game.points, 3)
