from typing import List, Optional, Type
from simpledominion.Pile import Pile
from simpledominion.game.card.CardInterface import CardInterface
from simpledominion.game.piles.Deck import DeckInterface

class HandInterface(Pile):

  _cards: List[CardInterface]
  _deck: DeckInterface

  def __init__(self, deck: DeckInterface) -> None:
    pass

  def isActionCard(self, idx: int) -> Optional[bool]:
    pass

  def play(self, idx: int) -> Optional[CardInterface]:
    pass

  def peek(self, idx: int) -> Optional[CardInterface]:
    pass

  def discardAllCards(self) -> List[CardInterface]:
    pass

  def drawFromDeck(self, count: int) -> bool:
    pass

class HandFactory:

  def create(self, deck: DeckInterface) -> HandInterface:
    return Hand(deck)

class Hand(HandInterface):

  _cards: List[CardInterface]
  _deck: DeckInterface

  def __init__(self, deck: DeckInterface) -> None:
    self._cards = list()
    self._deck = deck

  def isActionCard(self, idx: int) -> bool:
    if idx > len(self._cards):
      raise IndexError('You have less cards in hand than the index you were calling for')
    
    return self._cards[idx].cardType.isAction

  def play(self, idx: int) -> Optional[CardInterface]:
    card: Optional[CardInterface]
    if idx < len(self._cards):
      card = self._cards.pop(idx)
    else:
      card = None

    return card

  def peek(self, idx: int) -> Optional[CardInterface]:
    card: Optional[CardInterface]
    if idx < len(self._cards):
      card = self._cards[idx]
    else:
      card = None

    return card

  def discardAllCards(self) -> List[CardInterface]:
    cards: List[CardInterface] = self._cards
    self._cards = list()
    return cards

  def drawFromDeck(self, count: int) -> bool:
    self._cards.extend(self._deck.draw(count))
    return True
