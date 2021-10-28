from unittest import TestCase
from simpledominion.Play import PlayFactory, PlayInterface
from simpledominion.GameCardType import GameCardType, GAME_CARD_TYPE_ESTATE, GAME_CARD_TYPE_COPPER, GAME_CARD_TYPE_FESTIVAL
from simpledominion.CardInterface import CardInterface
from test.fake_card import FakeCard


class TestPlay(TestCase):

  def assertEmpty(self, play: PlayInterface):
    self.assertEqual(len(play._cards), 0)

  def setUp(self):
    playFactory = PlayFactory()
    self.play1 = playFactory.create()
    
  def test_add_cards_and_get_size(self):
    self.assertEmpty(self.play1)
    self.play1.putTo(FakeCard(GAME_CARD_TYPE_FESTIVAL))
    self.assertEqual(len(self.play1._cards), 1)
    self.play1.putTo(FakeCard(GAME_CARD_TYPE_ESTATE))
    self.play1.putTo(FakeCard(GAME_CARD_TYPE_ESTATE))
    self.assertEqual(len(self.play1._cards), 3)
    cards = self.play1.throwAll()
    self.assertEqual(len(cards), 3)
    self.assertEqual(len(self.play1._cards), 0)

