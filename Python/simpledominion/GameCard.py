from Python.simpledominion.GameCardType import GameCardType
from simpledominion.CardInterface import CardInterface
from simpledominion.GameCardType import GameCardType
from simpledominion.TurnStatus import TurnStatus

class GameCard(CardInterface):

  _type: GameCardType

  def __init__(self, type: GameCardType) -> None:
    self._type = type

  def evaluate(self, status: TurnStatus) -> None:
    status.actions += self._type.plusActions
    status.buys += self._type.plusBuys
    status.coins += self._type.plusCoins

  @property
  def cardType(self) -> GameCardType:
    return self._type

