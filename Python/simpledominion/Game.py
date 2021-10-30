from typing import Callable, Optional
from simpledominion.EndGameStrategy import EndGameStrategyInterface, EndGameStrategyFactory
from simpledominion.Turn import TurnFactory, TurnInterface
from simpledominion.TurnStatus import TurnStatus

PLAY_PHASE = 0
BUY_PHASE = 1

def whenGameRunning(f: Callable):
  def fun(*arg, **kwarg):
    self = arg[0]
    if self._gameEnded:
      raise Exception('Game has already ended. You can get result points by using accessing points parameter.')
    else:
      return f(*arg, **kwarg)
  return fun

class GameInterface:

  _turn: TurnInterface
  _points: int
  _gameEnded: bool
  _printWarnings: bool

  def playCard(self, handIdx: int) -> bool:
    pass

  def endPlayCardPhase(self) -> bool:
    pass

  def buyCard(self, buyCardIdx: int) -> bool:
    pass

  def calculatePoints(self) -> bool:
    pass

  def isEndOfGame(self) -> bool:
    pass

  def endTurn(self) -> bool:
    pass

  @property
  def turn(self) -> TurnInterface:
    pass

  @property
  def endGameStrategy(self) -> Optional[EndGameStrategyInterface]:
    pass

  @property
  def points(self) -> int:
    pass

  @property
  def printWarnings(self) -> bool:
    pass

  @printWarnings.setter
  def printWarnings(self, printW: bool) -> None:
    pass

class Game(GameInterface):

  _turn: TurnInterface
  _phase: int
  _points: int
  _gameEnded: bool
  _printWarnings: bool

  _endGameStrategy: EndGameStrategyInterface
  
  def __init__(self) -> None:
    turnFactory = TurnFactory()
    self._turn = turnFactory.create(TurnStatus(1, 1, 0))

    self._phase = PLAY_PHASE

    endGameFactory = EndGameStrategyFactory()
    self._endGameStrategy = endGameFactory.createAtLeastNEmptyDecks(self.turn.buyDecks, 3)

    self._points = 0
    self._gameEnded = False

    self._printWarnings = True
  
  @whenGameRunning
  def playCard(self, handIdx: int) -> bool:
    if self._phase != PLAY_PHASE:
      if self._printWarnings: print("WARNING! You are not in a play phase. End the turn and try again.")
      return False
    
    return self._turn.playCardFromHand(handIdx)
    
  @whenGameRunning
  def endPlayCardPhase(self) -> bool: 
    if self._phase != PLAY_PHASE:
      if self._printWarnings: print("WARNING! You are not in a play phase. End the turn and try again.")
      return False

    self._phase = BUY_PHASE
    return True

  @whenGameRunning
  def buyCard(self, buyCardIdx: int) -> bool:
    return self._turn.buyCard(buyCardIdx)

  def calculatePoints(self) -> bool:
    self._points = self.turn.calculatePoints()
    return True

  def isEndOfGame(self) -> bool:
    return self._endGameStrategy.isGameover()
  
  @whenGameRunning
  def endTurn(self) -> bool:
    if self._phase != BUY_PHASE:
      if self._printWarnings: print("WARNING! You are not in a buy phase, so you can't end the turn. End the action phase and try again.")
      return False

    result: bool = self._turn.endTurn()

    self._phase = PLAY_PHASE
    self._turn.turnStatus = TurnStatus(1, 1, 0)
    if self.isEndOfGame():
      self._points = self.turn.calculatePoints()
      self._gameEnded = True
    
    return result

  @property
  def turn(self) -> TurnInterface:
    return self._turn

  @property
  def endGameStrategy(self) -> EndGameStrategyInterface:
    return self._endGameStrategy
  
  @property
  def points(self) -> int:
    return self._points

  @property
  def printWarnings(self) -> bool:
    return self._printWarnings

  @printWarnings.setter
  def printWarnings(self, printW: bool) -> None:
    self._printWarnings = printW
