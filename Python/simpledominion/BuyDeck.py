from typing import List, Optional
from random import shuffle
from simpledominion.CardInterface import CardInterface

class BuyDeck:

  _cardCount: int

  _cards: List[CardInterface]

  def __init__(self) -> None:
    self._cardCount = 0
    self._cards = list()

  def addCard(self, card: CardInterface):
    self._cards.extend(card)
    self._cardCount += 1

  def buy(self) -> Optional[CardInterface]:
    if self._cardCount == 0:
      return None
    
    return self._cards.pop(0)

  def getTopCard(self) -> Optional[CardInterface]:
    if self._cardCount == 0:
      return None

    return self._cards[0]

  def isEmpty(self) -> bool:
    return self._cardCount == 0

  def shuffleDeck(self):
    shuffle(self._cards)
