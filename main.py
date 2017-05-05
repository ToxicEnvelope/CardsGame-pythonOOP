from Card import *
from Deck import *
from Player import *

if __name__ == '__main__':
	
	stdin = raw_input("Enter a name for player 1: ")
	Deck()
	p1 = Player(stdin)
	p1.isAlive()
