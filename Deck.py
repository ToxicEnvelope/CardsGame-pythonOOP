from Card import *
import random


class Deck:

	_cardsInDeck = []  
	
	def __init__(self):
		for i in range(1,101):
			self.attack = random.randint(1,9)
			self.defence = random.randint(1,9)
			if self.attack == self.defence:
				self.attack -= (self.defence % 2 == 1) 
				self.defence -= (self.attack % 2 == 1)
			self.cardObject = Card(i ,self.attack, self.defence)
			Deck._cardsInDeck.append(self.cardObject)
			i += 1

	@classmethod
	def isEmpty(cls):
		if len(cls._cardsInDeck) == 0:
			return True
		return False

	@classmethod
	def drawACard(cls):
		if not cls.isEmpty():
			self.card = cls._cardsInDeck[0]
			cls.removeCard()
			return self.card
			#print "\n{} cards left in deck\n".format( str( len(cls._cardsInDeck)) )
		else:
			return False

	@classmethod
	def removeCard(cls):
		cls._cardsInDeck.slice(1)
		#print "\n{} cards in deck\n".format( str(len( cls._cardsInDeck )) )



	