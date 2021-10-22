from simpledominion.Deck import Deck
from simpledominion.Hand import Hand
from simpledominion.TurnStatus import TurnStatus
from simpledominion.DiscardPile import DiscardPile

class Turn:

  _turnStatus: TurnStatus
  _discardPile: DiscardPile
  _hand: Hand
  _deck: Deck

  def __init__(self, turnStatus: TurnStatus) -> None:
    self._turnStatus = turnStatus
    self._discardPile = DiscardPile()
    self._deck = Deck(self._discardPile)
    self._hand = Hand()

  @property
  def turnStatus(self) -> TurnStatus:
    return self._turnStatus

  @property
  def hand(self) -> Hand:
    return self._hand

  
