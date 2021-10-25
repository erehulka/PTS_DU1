from simpledominion.CardInterface import CardInterface
from simpledominion.GameCardType import GameCardType

class FakeCard(CardInterface):
    def __init__(self, cardType: GameCardType):
        self._cardType = cardType

    @property
    def cardType(self):
    	return self._cardType
