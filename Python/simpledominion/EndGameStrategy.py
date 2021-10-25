from typing import Optional
from simpledominion.Game import Game

class EndGameStrategyInterface:

  def isGameover(self) -> bool:
    return False

class AtLeastNEmptyDecks(EndGameStrategyInterface):

  _game: Game
  _n: int

  def __init__(self, game: Game, n: int) -> None:
    self._game = game
    self._n = n
    
  def isGameover(self) -> bool:
    emptyDecks: int = 0
    for deck in self._game.turn.buyDecks:
      if deck.isEmpty():
        emptyDecks += 1

    
    return emptyDecks >= self._n
