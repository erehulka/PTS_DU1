from simpledominion.game.card.CardInterface import CardInterface
from simpledominion.Pile import Pile
from typing import Optional, List, Type
from random import shuffle

class DiscardPileInterface(Pile):

    def __init__(self, cards: List[CardInterface] = list()):
        pass

    def getTopCard(self) -> Optional[CardInterface]:
        pass

    def addCards(self, cards: List[CardInterface]) -> None:
        pass

    def getSize(self) -> Optional[int]:
        pass

    def getCards(self) -> List[CardInterface]:
        pass

class DiscardPileFactory:

    def create(self, cards: List[CardInterface]) -> DiscardPileInterface:
        return DiscardPile(cards)

    def createNonShuffling(self, cards: List[CardInterface]) -> DiscardPileInterface:
        return NonShufflingDiscardPile(cards)

class DiscardPile(DiscardPileInterface):
    _cards: List[CardInterface]

    def __init__(self, cards: List[CardInterface] = list()):
        self._cards = cards
        
    def getTopCard(self) -> Optional[CardInterface]: 
        return self._cards[-1] if self._cards else None
        
    def addCards(self, cards: List[CardInterface]) -> None:
        self._cards.extend(cards)
        
    def getSize(self) -> int:
        return len(self._cards)
        
    def getCards(self) -> List[CardInterface]:
        cards: List[CardInterface] = self._cards
        self._cards = []
        shuffle(cards)
        return cards
        
class NonShufflingDiscardPile(DiscardPileInterface):
    _cards: List[CardInterface]

    def __init__(self, cards: List[CardInterface]):
        self._cards = cards

    def getTopCard(self) -> Optional[CardInterface]:
        return self._cards[-1] if self._cards else None

    def addCards(self, cards: List[CardInterface]) -> None:
        self._cards.extend(cards)

    def getSize(self) -> int:
        return len(self._cards)

    def getCards(self) -> List[CardInterface]:
        cards: List[CardInterface] = self._cards
        self._cards = []
        return cards
