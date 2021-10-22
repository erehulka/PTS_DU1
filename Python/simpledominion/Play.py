from typing import List
from simpledominion.CardInterface import CardInterface

class Play:

  _cards: List[CardInterface]


  def __init__(self) -> None:
    self._cards = list()

  def putTo(self, card: CardInterface) -> None:
    self._cards.extend(card)

  def throwAll(self) -> List[CardInterface]:
    to_return: List[CardInterface] = self._cards
    self._cards = list()
    return to_return
