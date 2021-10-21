from typing import List
from simpledominion.CardInterface import CardInterface
from simpledominion.DiscardPile import DiscardPile

class Deck:

  _discardPile: DiscardPile

  def draw(self, count: int) -> List[CardInterface]:
    pass
