# Python Program illustrating
# numpy.random.rand() method

import random
class Game(object):

	def __init__(self):
		self.array = [[random.randint(0,100) for e in range(8)]for e in range(8)]
		self.source = int(input("enter the number of your choice from 0-100\n"))

		
	def run(self):
		f = 0
		for i in range(8):
			for j in range(8):
				if self.source == self.array[i][j]:
					f=f+1
				else:
					f=0
		if (f==0):
			print("Element not found so you loose.")
		else:
			print("Element found")

