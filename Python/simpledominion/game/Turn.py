from typing import List, Optional, Type
from simpledominion.game.card.GameCardType import GameCardType
from simpledominion.game.piles.BuyDeck import BuyDeckInterface
from simpledominion.game.piles.Play import PlayFactory, PlayInterface
from simpledominion.game.card.CardInterface import CardInterface
from simpledominion.game.piles.Deck import DeckInterface, DeckFactory
from simpledominion.game.player.Hand import HandFactory, HandInterface
from simpledominion.game.TurnStatus import TurnStatus
from simpledominion.game.piles.DiscardPile import DiscardPileFactory, DiscardPileInterface

class TurnInterface:

  _turnStatus: TurnStatus
  _discardPile: DiscardPileInterface
  _hand: HandInterface
  _deck: DeckInterface
  _play: PlayInterface
  _buyDecks: List[BuyDeckInterface]

  def __init__(self, turnStatus: TurnStatus) -> None:
    pass

  def addBuyDeck(self, buyDeck: BuyDeckInterface) -> bool:
    pass

  def buyCard(self, buyCardIdx: int) -> bool:
    pass

  def calculatePoints(self) -> int:
    pass

  def playCardFromHand(self, idx: int) -> bool:
    pass

  def endTurn(self) -> bool:
    pass

  def throwPlayAndHandCardsToDiscardPile(self) -> bool:
    pass

  @property
  def turnStatus(self) -> TurnStatus:
    pass

  @turnStatus.setter
  def turnStatus(self, status: TurnStatus):
    pass

  @property
  def hand(self) -> HandInterface:
    pass

  @property
  def buyDecks(self) -> List[BuyDeckInterface]:
    pass

  @property
  def deck(self) -> DeckInterface:
    pass

class TurnFactory:

  def create(self, status: TurnStatus) -> TurnInterface:
    return Turn(status)

class Turn(TurnInterface):

  _turnStatus: TurnStatus
  _discardPile: DiscardPileInterface
  _hand: HandInterface
  _deck: DeckInterface
  _play: PlayInterface
  _buyDecks: List[BuyDeckInterface]

  def __init__(self, turnStatus: TurnStatus) -> None:
    self._turnStatus = turnStatus

    dpileFactory = DiscardPileFactory()
    self._discardPile = dpileFactory.create([])

    deckFactory = DeckFactory()
    self._deck = deckFactory.create(self._discardPile)

    handFactory = HandFactory()
    self._hand = handFactory.create(self._deck)

    playFactory = PlayFactory()
    self._play = playFactory.create()

    self._buyDecks = list()

  def addBuyDeck(self, buyDeck: BuyDeckInterface) -> bool:
    self._buyDecks.append(buyDeck)
    return True

  def buyCard(self, buyCardIdx: int) -> bool:
    if buyCardIdx > len(self._buyDecks) or self._turnStatus.buys == 0:
      return False

    cardType: Optional[GameCardType] = self._buyDecks[buyCardIdx].getCardInfo()
    card: Optional[CardInterface] = None
    if cardType is not None and cardType.cost <= self._turnStatus.coins:
      self._turnStatus.coins -= cardType.cost
      self._turnStatus.buys -= 1
      card = self._buyDecks[buyCardIdx].buy()

    if card is None:
      return False

    card.evaluate(self._turnStatus)
    self._discardPile.addCards([card])
    return True

  def calculatePoints(self) -> int:
    return self.hand.calculatePoints() + self.deck.calculatePoints() + self._discardPile.calculatePoints() + self._play.calculatePoints()

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
