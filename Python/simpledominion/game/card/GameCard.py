from typing import Type
from simpledominion.game.card.GameCardType import GameCardType
from simpledominion.game.card.CardInterface import CardInterface
from simpledominion.game.card.GameCardType import GameCardType
from simpledominion.game.TurnStatus import TurnStatus

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

class GameCardFactory:

  _class: Type[CardInterface]

  def __init__(self) -> None:
    self._class = GameCard

  def create(self, type: GameCardType) -> CardInterface:
    return self._class(type)
