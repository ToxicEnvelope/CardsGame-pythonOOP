from Deck import *


class Player:
    
	_cardsInHand = None

	def __init__(self, name):
	    self.name = name
	    self.state = 1
	    self.health = 20

	def isAlive(self):
		if self.health <= 0 :
			print "{} has been destroyed".fromat( self.name ) 
		else:
			print "{} got {} health".format( self.name, 
				                        str( self.health ) )
	
	@classmethod
	def getCardFromDeck(cls):
		if cls._cardsInHand == None:
			cls._cardsInHand = Deck.drawACard()
			if cls._cardsInHand == None:
				return False
			return True

	@classmethod
	def reduceLife(cls): 
		if cls.isActive() == False:
			return False
		cls.health -= 1
		return True

	@classmethod
	def isActive(cls):
		if cls.state == 0:
			return True
		return False