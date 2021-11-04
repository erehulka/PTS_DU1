from simpledominion.game.card.CardInterface import CardInterface
from simpledominion.game.card.GameCardType import GameCardType

class FakeCard(CardInterface):
    def __init__(self, cardType: GameCardType):
        self._cardType = cardType

    @property
    def cardType(self):
    	return self._cardType
