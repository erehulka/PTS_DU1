from random import shuffle
from typing import List, Optional, Type
from simpledominion.CardInterface import CardInterface
from simpledominion.DiscardPile import DiscardPileInterface

class DeckInterface:

  def __init__(self, discardPile: DiscardPileInterface) -> None:
    pass

  def addCard(self, card: CardInterface) -> None:
    pass

  def shuffleDeck(self) -> None:
    pass

  def draw(self, count: int) -> List[CardInterface]:
    pass

class DeckFactory:

  _class: Type[DeckInterface]

  _discardPile: DiscardPileInterface

  def __init__(self, dPile: DiscardPileInterface) -> None:
    self._class = Deck
    self._discardPile = dPile

  def create(self) -> DeckInterface:
    return self._class(self._discardPile)

class Deck(DeckInterface):

  _discardPile: DiscardPileInterface

  _cards: List[CardInterface]

  def __init__(self, discardPile: DiscardPileInterface) -> None:
    self._cards = list()
    self._discardPile = discardPile

  def addCard(self, card: CardInterface) -> None:
    self._cards.append(card)

  def shuffleDeck(self) -> None:
    shuffle(self._cards)

  def draw(self, count: int) -> List[CardInterface]:
    if count > len(self._cards):
      self._cards.extend(self._discardPile.shuffle())
    if count > len(self._cards):
      count = len(self._cards)

    to_return = self._cards[:count]
    self._cards = self._cards[count:]
    return to_return
