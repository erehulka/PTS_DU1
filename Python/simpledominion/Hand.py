from typing import List, Optional
from simpledominion.CardInterface import CardInterface
from simpledominion.Deck import Deck

class Hand:

  _cards: List[CardInterface]
  _deck: Deck

  def isActionCard(self, idx: int) -> bool:
    if idx > len(self._cards):
      raise IndexError('You have less cards in hand than the index you were calling for')
    
    return self._cards[idx].cardType.isAction

  def play(self, idx: int) -> Optional[CardInterface]:
    pass
