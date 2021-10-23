from typing import Optional
from simpledominion.Turn import Turn
from simpledominion.TurnStatus import TurnStatus

PLAY_PHASE = 0
BUY_PHASE = 1

class Game:

  _turn: Turn
  _phase: int
  
  def __init__(self) -> None:
    self._turn = Turn(TurnStatus(1, 1, 0))
    self._phase = PLAY_PHASE
  
  def playCard(self, handIdx: int) -> bool:
    if self._phase != PLAY_PHASE:
      print("WARNING! You are not in a play phase. End the turn and try again.")
      return False
    
    return self._turn.hand.play(handIdx)
    

  def endPlayCardPhase(self) -> bool: 
    if self._phase != PLAY_PHASE:
      print("WARNING! You are not in a play phase. End the turn and try again.")
      return False

    self._phase = BUY_PHASE
    return True

  def buyCard(self, buyCardIdx: int) -> bool:
    return self._turn.buyCard(buyCardIdx)
  
  def endTurn(self) -> bool:
    if self._phase != BUY_PHASE:
      print("WARNING! You are not in a buy phase, so you can't end the turn. End the action phase and try again.")
      return False

    self._turn.endTurn()

    self._phase = PLAY_PHASE
    self._turn.turnStatus = TurnStatus(1, 1, 0)
    # TODO Not the end of the game?
