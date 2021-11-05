from typing import List, Optional, Type
from simpledominion.game.card.CardInterface import CardInterface

class PlayInterface:

  _cards: List[CardInterface]

  def __init__(self) -> None:
    pass

  def putTo(self, card: CardInterface) -> None:
    pass

  def throwAll(self) -> List[CardInterface]:
    pass

  def calculatePoints(self) -> int:
    pass

class PlayFactory:

  _class: Type[PlayInterface]

  def __init__(self) -> None:
    self._class = Play

  def create(self) -> PlayInterface:
    return self._class()

class Play(PlayInterface):

  _cards: List[CardInterface]

  def __init__(self) -> None:
    self._cards = list()

  def putTo(self, card: CardInterface) -> None:
    self._cards.append(card)

  def throwAll(self) -> List[CardInterface]:
    to_return: List[CardInterface] = self._cards
    self._cards = list()
    return to_return

  def calculatePoints(self) -> int:
    points = 0
    for card in self._cards:
      points += card.cardType.points
    return points