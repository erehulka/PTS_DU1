from typing import List, Optional, Type
from random import shuffle
from simpledominion.GameCardType import GameCardType
from simpledominion.GameCard import GameCardFactory
from simpledominion.CardInterface import CardInterface

class BuyDeckInterface:

  _cardCount: int

  def __init__(self, type: GameCardType, count: int) -> None:
    pass

  def buy(self) -> Optional[CardInterface]:
    pass

  def getCardInfo(self) -> Optional[GameCardType]:
    pass

  def isEmpty(self) -> Optional[bool]:
    pass

class BuyDeckFactory:

  _class: Type[BuyDeckInterface]

  def __init__(self) -> None:
    self._class = BuyDeck

  def create(self, type: GameCardType, count: int) -> BuyDeckInterface:
    return self._class(type, count)

class BuyDeck(BuyDeckInterface):

  _cardCount: int

  _cardType: GameCardType

  _factory: GameCardFactory

  def __init__(self, type: GameCardType, count: int) -> None:
    self._cardCount = count
    self._cardType = type
    self._factory = GameCardFactory()
  
  def buy(self) -> Optional[CardInterface]:
    if self._cardCount == 0:
      return None

    self._cardCount -= 1
    
    return self._factory.create(self._cardType)

  def getCardInfo(self) -> GameCardType:
    return self._cardType

  def isEmpty(self) -> bool:
    return self._cardCount == 0
