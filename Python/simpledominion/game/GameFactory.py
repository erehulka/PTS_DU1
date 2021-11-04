from typing import Type
from simpledominion.game.Game import GameInterface, Game
from simpledominion.game.piles.BuyDeck import BuyDeckFactory
from simpledominion.game.card.GameCard import GameCardFactory
from simpledominion.game.card.GameCardType import GAME_CARD_TYPE_ESTATE, GAME_CARD_TYPE_COPPER, GAME_CARD_TYPE_FESTIVAL, GAME_CARD_TYPE_MARKET, \
  GAME_CARD_TYPE_LABORATORY, GAME_CARD_TYPE_SMITHY, GAME_CARD_TYPE_VILLAGE

class GameFactory:

  _class: Type[GameInterface]

  def __init__(self) -> None:
    self._class = Game

  def createClassicGame(self) -> GameInterface:
    game = Game()
    buyDeckFactory = BuyDeckFactory()

    game.turn.addBuyDeck(buyDeckFactory.create(GAME_CARD_TYPE_ESTATE, 10))
    game.turn.addBuyDeck(buyDeckFactory.create(GAME_CARD_TYPE_COPPER, 10))
    game.turn.addBuyDeck(buyDeckFactory.create(GAME_CARD_TYPE_FESTIVAL, 10))
    game.turn.addBuyDeck(buyDeckFactory.create(GAME_CARD_TYPE_MARKET, 10))
    game.turn.addBuyDeck(buyDeckFactory.create(GAME_CARD_TYPE_LABORATORY, 10))
    game.turn.addBuyDeck(buyDeckFactory.create(GAME_CARD_TYPE_SMITHY, 10))
    game.turn.addBuyDeck(buyDeckFactory.create(GAME_CARD_TYPE_VILLAGE, 10))

    cardFactory = GameCardFactory()
    for i in range(3):
      game.turn.deck.addCard(cardFactory.create(GAME_CARD_TYPE_ESTATE))
    for i in range(7):
      game.turn.deck.addCard(cardFactory.create(GAME_CARD_TYPE_COPPER))
    game.turn.deck.shuffleDeck()
    game.turn.hand.drawFromDeck(5)

    return game