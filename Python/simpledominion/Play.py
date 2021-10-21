from typing import List
from simpledominion.DiscardPile import DiscardPile
from simpledominion.CardInterface import CardInterface

class Play:

  _cards: List[CardInterface]

  _discardPile: DiscardPile

  def __init__(self, discardPile: DiscardPile) -> None:
    self._cards = list()
    self._discardPile = discardPile

  def putTo(self, card: CardInterface) -> None:
    self._cards.extend(card)

  def throwAll(self) -> List[CardInterface]:
    to_return: List[CardInterface] = self._cards
    self._cards = list()
    return to_return
