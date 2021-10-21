
from typing import List, Tuple, Optional
from simpledominion.SimpleDominionInterface import SimpleDominionInterface, GameState
from simpledominion.Game import Game

class SimpleDominion(SimpleDominionInterface):
    
  _game: Game

  def playCard(self, handIdx: int) -> Optional[GameState]:
    if self._game.playCard(handIdx):
      pass

    return None
  
  def endPlayCardPhase(self) -> Optional[GameState]:
    pass
  def buyCard(self, buyCardIdx: int) -> Optional[GameState]:
    pass
  def endTurn(self) -> Optional[GameState]:
    pass
