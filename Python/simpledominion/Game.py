from typing import Optional
from simpledominion.EndGameStrategy import EndGameStrategyInterface, AtLeastNEmptyDecks
from simpledominion.Turn import TurnFactory, TurnInterface
from simpledominion.TurnStatus import TurnStatus

PLAY_PHASE = 0
BUY_PHASE = 1

DEFAULT_END_STRATEGY = AtLeastNEmptyDecks

class GameInterface:

  _turn: TurnInterface

  def playCard(self, handIdx: int) -> bool:
    pass

  def endPlayCardPhase(self) -> bool:
    pass

  def buyCard(self, buyCardIdx: int) -> bool:
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

class Game(GameInterface):

  _turn: TurnInterface
  _phase: int

  _endGameStrategy: EndGameStrategyInterface
  
  def __init__(self) -> None:
    turnFactory = TurnFactory()
    self._turn = turnFactory.create(TurnStatus(1, 1, 0))

    self._phase = PLAY_PHASE
    self._endGameStrategy = DEFAULT_END_STRATEGY(self, 3)
  
  def playCard(self, handIdx: int) -> bool:
    if self._phase != PLAY_PHASE:
      print("WARNING! You are not in a play phase. End the turn and try again.")
      return False
    
    return self._turn.playCardFromHand(handIdx)
    

  def endPlayCardPhase(self) -> bool: 
    if self._phase != PLAY_PHASE:
      print("WARNING! You are not in a play phase. End the turn and try again.")
      return False

    self._phase = BUY_PHASE
    return True

  def buyCard(self, buyCardIdx: int) -> bool:
    return self._turn.buyCard(buyCardIdx)

  def isEndOfGame(self) -> bool:
    return self._endGameStrategy.isGameover()
  
  def endTurn(self) -> bool:
    if self._phase != BUY_PHASE:
      print("WARNING! You are not in a buy phase, so you can't end the turn. End the action phase and try again.")
      return False

    result: bool = self._turn.endTurn()

    self._phase = PLAY_PHASE
    self._turn.turnStatus = TurnStatus(1, 1, 0)
    if self.isEndOfGame():
      pass
      # TODO Evaluate end of game
    
    return result

  @property
  def turn(self) -> TurnInterface:
    return self._turn

  @property
  def endGameStrategy(self) -> EndGameStrategyInterface:
    return self._endGameStrategy
