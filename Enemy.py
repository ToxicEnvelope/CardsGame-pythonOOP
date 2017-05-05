from Deck import *


class Enemy:
    
	_cardsInHand = None

	def __init__(self):
	    self.name = "Computer"
	    self.health = 20

	def isAlive(self):
		if self.health <= 0 :
			print "{} has been destroyed".fromat( self.name ) 
		else:
			print "{} got {} health".format( self.name, 
				                        str( self.health ) )
	
	@classmethod
	def drawACard(cls):
		if cls._cardsInHand == None:
			if len(Deck._cardsInDeck) > 0:
				cls._cardsInHand = Deck._cardsInDeck[0]
				print "\nComputer drew a card from deck\nCARD INFO:\n{}".format( str( cls._cardsInHand.__dict__ ) )
