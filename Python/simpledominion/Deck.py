from random import shuffle
from typing import List
from simpledominion.CardInterface import CardInterface
from simpledominion.DiscardPile import DiscardPile

class Deck:

  _discardPile: DiscardPile

  _cards: List[CardInterface]

  def __init__(self, discardPile: DiscardPile) -> None:
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
      raise Exception("There are not this many cards in deck.")

    to_return = self._cards[:count]
    self._cards = self._cards[count:]
    return to_return
