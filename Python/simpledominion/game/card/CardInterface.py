from simpledominion.game.TurnStatus import TurnStatus
from simpledominion.game.card.GameCardType import GameCardType

class CardInterface:

    def __init__(self, type: GameCardType) -> None:
        pass

    def evaluate(self, TurnStatus) -> None:
    	pass
    @property
    def cardType(self) -> GameCardType:
    	pass


