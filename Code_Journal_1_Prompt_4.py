import sys			#using this to import sys
class Animal:		#name of the class

	#Using this to print the length of legs, arms, number of eyes, and if it has a tail. 
	def print(self):
		print("Here is my Animal.")
		print(f'Length of the arms = {self.larms}') #Float length of arms
		print(f'Length of the legs = {self.llegs}') #Float length of legs
		print(f'Number of eyes = {self.neyes}')	 #Int number of eyes
		print(f'Does it have a tail? {self.Tail}')	 #Bool if it has tail

	#Use the initialization to show the different parts of the animal.
	def __init__(self,larms=0.0, llegs = 1.0, neyes = 2, Tail = True):
		self.larms = larms
		self.llegs = llegs
		self.neyes = neyes
		self.Tail = Tail


def main():

	#default numbers for each variable
	larms = 0.0
	llegs = 12.0
	neyes = 2
	Tail = True

	#Associate each variable with each part of the class.
	my_animal = Animal(larms = larms, llegs = llegs, neyes = neyes, Tail = True)

	#Now to print out the information of the animal.
	my_animal.print()

if __name__ == '__main__':
	main()