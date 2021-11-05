from typing import List, Optional, Type
from simpledominion.game.card.CardInterface import CardInterface

class Pile:

  _cards: List[CardInterface]

  def calculatePoints(self) -> int:
    points = 0
    for card in self._cards:
      points += card.cardType.points
    return points
