

class Player:
    
    _cardInHand = 0

	def __init__(self, name):
		self.name = name
		self.health = 20

	def isAlive(self):
		if self.health <= 0 :
			print "{} has been destroyed".fromat( self.name ) 
		else:
			print "{} got {} health".format( self.name, 
				                        str( self.health ) )
	def drawACard(self):
		