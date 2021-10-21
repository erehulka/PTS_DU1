from simpledominion.Deck import Deck
from simpledominion.Hand import Hand
from simpledominion.TurnStatus import TurnStatus
from simpledominion.DiscardPile import DiscardPile

class Turn:

  _turnStatus: TurnStatus
  _discardPile: DiscardPile
  _hand: Hand
  _deck: Deck

  def __init__(self) -> None:
    pass

  