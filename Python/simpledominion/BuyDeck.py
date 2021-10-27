from typing import List, Optional, Type
from random import shuffle
from simpledominion.CardInterface import CardInterface

class BuyDeckInterface:

  def addCard(self, card: CardInterface) -> Optional[bool]:
    pass

  def buy(self) -> Optional[CardInterface]:
    pass

  def getTopCard(self) -> Optional[CardInterface]:
    pass

  def isEmpty(self) -> Optional[bool]:
    pass

  def shuffleDeck(self) -> None:
    pass

class BuyDeckFactory:

  _class: Type[BuyDeckInterface]

  def __init__(self) -> None:
    self._class = BuyDeck

  def create(self) -> BuyDeckInterface:
    return self._class()

class BuyDeck(BuyDeckInterface):

  _cardCount: int

  _cards: List[CardInterface]

  def __init__(self) -> None:
    self._cardCount = 0
    self._cards = list()

  def addCard(self, card: CardInterface) -> bool:
    self._cards.append(card)
    self._cardCount += 1
    return True

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

  def shuffleDeck(self) -> None:
    shuffle(self._cards)
