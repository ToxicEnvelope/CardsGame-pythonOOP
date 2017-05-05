class Enemy:

	def __init__(self):
		self.name = "Computer"
		self.health = 20

	def isAlive(self):
		if self.health <= 0:
			print "{} has been destroyed".fromat( self.name ) 
		else:
			self.health -= 1
			print "{}, you left with {} health".format( self.name , str( self.health ) )

	
