from typing import List, Optional
from simpledominion.BuyDeck import BuyDeckInterface
from simpledominion.Play import PlayFactory, PlayInterface
from simpledominion.CardInterface import CardInterface
from simpledominion.Deck import DeckInterface, DeckFactory
from simpledominion.Hand import HandFactory, HandInterface
from simpledominion.TurnStatus import TurnStatus
from simpledominion.DiscardPile import DiscardPileFactory, DiscardPileInterface

class Turn:

  _turnStatus: TurnStatus
  _discardPile: DiscardPileInterface
  _hand: HandInterface
  _deck: DeckInterface
  _play: PlayInterface
  _buyDecks: List[BuyDeckInterface]

  def __init__(self, turnStatus: TurnStatus) -> None:
    self._turnStatus = turnStatus

    dpileFactory = DiscardPileFactory()
    self._discardPile = dpileFactory.create()

    deckFactory = DeckFactory(self._discardPile)
    self._deck = deckFactory.create()

    handFactory = HandFactory(self._deck)
    self._hand = handFactory.create()

    playFactory = PlayFactory()
    self._play = playFactory.create()

    self._buyDecks = list()

  def addBuyDeck(self, buyDeck: BuyDeckInterface) -> bool:
    self._buyDecks.append(buyDeck)
    return True

  def buyCard(self, buyCardIdx: int) -> bool:
    if buyCardIdx > len(self._buyDecks) or self._turnStatus.buys == 0:
      return False

    card: Optional[CardInterface] = self._buyDecks[buyCardIdx].getCardInfo()
    if card is not None and card.cardType.cost <= self._turnStatus.coins:
      self._turnStatus.coins -= card.cardType.cost
      self._turnStatus.buys -= 1
      card = self._buyDecks[buyCardIdx].buy()

    if card is None:
      return False

    card.evaluate(self._turnStatus)
    self._discardPile.addCards([card])
    return True

  def playCardFromHand(self, idx: int) -> bool:
    card: Optional[CardInterface] = self._hand.play(idx)
    if card is None:
      return False

    if card.cardType.isAction and self._turnStatus.actions == 0:
      return False

    if card.cardType.isAction:
      self._turnStatus.actions -= 1
    card.evaluate(self._turnStatus)
    if card.cardType.plusCards:
      self.hand.drawFromDeck(card.cardType.plusCards)
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

  @turnStatus.setter
  def turnStatus(self, status: TurnStatus):
    self._turnStatus = status

  @property
  def hand(self) -> HandInterface:
    return self._hand

  @property
  def buyDecks(self) -> List[BuyDeckInterface]:
    return self._buyDecks

  @property
  def deck(self) -> DeckInterface:
    return self._deck
