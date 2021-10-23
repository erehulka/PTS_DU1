from typing import List, Optional
from simpledominion.BuyDeck import BuyDeck
from simpledominion.Play import Play
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
  _play: Play
  _buyDecks: List[BuyDeck]

  def __init__(self, turnStatus: TurnStatus) -> None:
    self._turnStatus = turnStatus
    self._discardPile = DiscardPile()
    self._deck = Deck(self._discardPile)
    self._hand = Hand(self._deck)
    self._play = Play(self._discardPile)
    self._buyDecks = list()

  def addBuyDeck(self, buyDeck: BuyDeck) -> bool:
    self._buyDecks.extend(buyDeck)
    return True

  def buyCard(self, buyCardIdx: int) -> bool:
    if buyCardIdx > len(self._buyDecks) or self._turnStatus.buys == 0:
      return False

    card: Optional[CardInterface] = self._buyDecks[buyCardIdx].getTopCard()
    if card is not None and card.cardType.cost <= self._turnStatus.coins:
      self._turnStatus.coins -= card.cardType.cost
      self._turnStatus.buys -= 1
      card = self._buyDecks[buyCardIdx].buy()

    if card is None:
      return False

    card.evaluate(self._turnStatus)
    self._discardPile.addCards([card])

  def playCardFromHand(self, idx: int) -> bool:
    card: Optional[CardInterface] = self._hand.play(idx)
    if card is None:
      return False

    card.evaluate(self._turnStatus)
    self._play.putTo(card)
    return True

  def endTurn(self) -> bool:
    result: bool = True
    result = result and self.throwPlayAndHandCardsToDiscardPile()
    result = result and self._hand.drawFromDeck(5)
    return result

  def throwPlayAndHandCardsToDiscardPile(self) -> bool:
    self._discardPile.addCards(self._play.throwAll())
    self._discardPile.addCards(self._hand.discardAllCards())
    return True

  @property
  def turnStatus(self) -> TurnStatus:
    return self._turnStatus

  @property
  def hand(self) -> Hand:
    return self._hand

  
