from Player import *
from Enemy import *
from Deck import *


class Game:

	_playerState = True
	_handler = None

	def __init__(self, player, pc):
		self.name = player
		self.bot = pc
		self.players = [
						Player( self.name ),
						Enemy( self.bot ) 
					   ]
		Game._handler = self.players
		print str(Game._handler)

	@classmethod
	def runGame(cls):
		while True:
			for x in range(0, len(cls._handler) ):
				if cls._handler[x].getCardsFromDeck() == False:
					cls.kickPlayer( cls._handler[x] )
				else:
					cls.battle( cls._handler.slice(1), cls._handler.slice(2) )
					cls.getPlayersState( x )
					if cls.getPlayersState() == 0:
						cls.kickPlayer( cls._handler[x] )
			
	@classmethod
	def battle(cls, player1, player2):
		self.card1 = cls.player1._cardsInHand
		self.card2 = cls.player2._cardsInHand	
		if self.card1.attack < self.card2.defence:
			player1.reduceLives()
		else:
			player2.reduceLives()

	@classmethod
	def getPlayersState(cls, x):
		self.x = x
		self.player1 = cls.players[ self.x ]
		return self.player1.state

	@classmethod
	def kickPlayer(cls, player):
		self.player = player
		cls.players
		cls.players.pop( self.player )
		if len(cls.players) == 1:
			cls.endGame()

	@classmethod
	def endGame(cls):
		self.winner = cls.players[0]
		return False
