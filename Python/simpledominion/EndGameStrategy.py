from typing import Optional
from simpledominion.Game import Game

class EndGameStrategyInterface:

  def isGameover(self) -> Optional[bool]:
    pass

class EndGameStrategyOne(EndGameStrategyInterface):

  _game: Game

  def __init__(self, game: Game) -> None:
    self._game = game

  def isGameover(self) -> Optional[bool]:
    return super().isGameover()


class AtLeastNEmptyDecks(EndGameStrategyInterface):

  _game: Game
  _n: int

  def __init__(self, game: Game, n: int) -> None:
    self._game = game
    self._n = n
    
  def isGameover(self) -> Optional[bool]:
    return super().isGameover() # TODO Implement decks and check if at least n are empty
