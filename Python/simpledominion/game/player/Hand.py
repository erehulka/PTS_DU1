from typing import List, Optional, Type
from simpledominion.game.card.CardInterface import CardInterface
from simpledominion.game.piles.Deck import DeckInterface

class HandInterface:

  _cards: List[CardInterface]
  _deck: DeckInterface

  def __init__(self, deck: DeckInterface) -> None:
    pass

  def isActionCard(self, idx: int) -> Optional[bool]:
    pass

  def play(self, idx: int) -> Optional[CardInterface]:
    pass

  def discardAllCards(self) -> List[CardInterface]:
    pass

  def calculatePoints(self) -> int:
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

  def calculatePoints(self) -> int:
    points = 0
    for card in self._cards:
      points += card.cardType.points
    return points

  def drawFromDeck(self, count: int) -> bool:
    self._cards.extend(self._deck.draw(count))
    return True
