from typing import List, Optional
from simpledominion.CardInterface import CardInterface
from simpledominion.Deck import Deck
from simpledominion.Hand import Hand
from simpledominion.TurnStatus import TurnStatus
from simpledominion.DiscardPile import DiscardPile

class Turn:

  _turnStatus: TurnStatus
  _discardPile: DiscardPile
  _hand: Hand
  _deck: Deck

  _playCards: List[CardInterface]

  def __init__(self, turnStatus: TurnStatus) -> None:
    self._turnStatus = turnStatus
    self._discardPile = DiscardPile()
    self._deck = Deck(self._discardPile)
    self._hand = Hand(self._deck)
    self._playCards = list()

  def playCardFromHand(self, idx: int) -> bool:
    card: Optional[CardInterface] = self._hand.play(idx)
    if card is None:
      return False

    card.evaluate(self._turnStatus)
    self._playCards.extend(card)
    return True

  def endTurn(self) -> bool:
    result: bool = True
    result = result and self.throwPlayAndHandCardsToDiscardPile()
    result = result and self._hand.drawFromDeck(5)
    return result

  def throwPlayAndHandCardsToDiscardPile(self) -> bool:
    self._discardPile.addCards(self._playCards)
    self._playCards = list()
    self._discardPile.addCards(self._hand.discardAllCards())
    return True

  @property
  def turnStatus(self) -> TurnStatus:
    return self._turnStatus

  @property
  def hand(self) -> Hand:
    return self._hand

  
