from typing import List, Optional
from simpledominion.game.card.GameCardType import GAME_CARD_TYPE_PROVINCE
from simpledominion.game.piles.BuyDeck import BuyDeckInterface

class EndGameStrategyInterface:

  def isGameover(self) -> bool:
    pass

class EndGameStrategyFactory:

  def __init__(self) -> None:
    pass

  def createAtLeastNEmptyDecks(self, buyDecks: List[BuyDeckInterface], n: int) -> EndGameStrategyInterface:
    return AtLeastNEmptyDecks(buyDecks, n)

class AtLeastNEmptyDecks(EndGameStrategyInterface):

  _buyDecks: List[BuyDeckInterface]
  _n: int

  def __init__(self, buyDecks: List[BuyDeckInterface], n: int) -> None:
    self._buyDecks = buyDecks
    self._n = n
    
  def isGameover(self) -> bool:
    emptyDecks: int = 0
    for deck in self._buyDecks:
      if deck.isEmpty():
        emptyDecks += 1

    return emptyDecks >= self._n

class ProvinceDeckEmpty(EndGameStrategyInterface):

  _buyDecks: List[BuyDeckInterface]

  def __init__(self, buyDecks: List[BuyDeckInterface]) -> None:
    self._buyDecks = buyDecks

  def isGameover(self) -> bool:
    for deck in self._buyDecks:
      if deck.getCardInfo() == GAME_CARD_TYPE_PROVINCE and deck.isEmpty(): return True

    return False
