import uuid

class Card:

		def __init__(self, num, attack, defence):
			self.num = num
			self.id = uuid.uuid4()
			self.attack = attack
			self.defence = defence
			print "\nCard #{}\nID: {}\nAttack: {}\nDefence: {}\n".format( str( self.num ),
																		  str( self.id ),
																		  str( self.attack),
																		  str( self.defence) )

		