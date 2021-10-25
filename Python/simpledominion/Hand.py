from typing import List, Optional
from simpledominion.CardInterface import CardInterface
from simpledominion.Deck import Deck

class Hand:

  _cards: List[CardInterface]
  _deck: Deck

  def __init__(self, deck: Deck) -> None:
    self._cards = list()
    self._deck = deck

  def isActionCard(self, idx: int) -> bool:
    if idx > len(self._cards):
      raise IndexError('You have less cards in hand than the index you were calling for')
    
    return self._cards[idx].cardType.isAction

  def play(self, idx: int) -> Optional[CardInterface]:
    card: Optional[CardInterface]
    if idx < len(self._cards):
      card = self._cards[idx]
      newCards = self._cards[:idx]
      newCards.extend(self._cards[idx+1:])
      self._cards = newCards
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
