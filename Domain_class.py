from __future__ import print_function
from random import randint


all_treasure = ["Sword","Gold Coin","Umbrella","Gumball","Egg","Sandwich","Necklace","Mysterious Artifact","Scroll","Pretty Rock"]

class Domain:

	number_of_domains = 0
	number_of_possible_creatures = 4
	dimensions = 0
	
	
	number_of_dif_treasures = 10
	
	def __init__(self,x,y,danger,number): #instance variables unique to each instance
		self.x = x
		self.y = y
		
		self.domain_num = number
		
		self.danger = danger
		
		self.creatures = []  #should be a list of DICTIONARIES {name,danger level,population}
		self.phys_features = []
		self.dangers = []  
		self.treasure = []
		
		self.name = ""  #what this region is called
		
		#people currently in this domain (to remove: list.remove(person))
		self.majors_here = []
		self.normals_here = []
				

		
	def add_creature(self,which_one):
		if which_one == 0:
			self.creatures.append({"Name":"Wolves" , "Name-Singular":"Wolf" , "Danger Level":3 , "Population":10})
		elif which_one == 1:
			self.creatures.append({"Name":"Tigers" , "Name-Singular":"Tiger" , "Danger Level":4 , "Population":10})
		elif which_one == 2:
			self.creatures.append({"Name":"Raptors" , "Name-Singular":"Raptor" , "Danger Level":3 , "Population":10})
		elif which_one == 3:
			self.creatures.append({"Name":"Aardvarks" , "Name-Singular":"Aardvark" , "Danger Level":2 , "Population":10})
			
			
	def add_treasure(self,which_one):
		self.treasure.append(all_treasure[which_one])
		
	
			
	def update_name(self):
	
		firstword = ""
		if len(self.creatures) > 0:
			firstword = self.creatures[0]["Name-Singular"] + "\'s"
		else:
			firstword = "Empty"
			
		secondword = ""
		rand = randint(0,4)
		#maybe later make this depending on what's actually IN the domains...
		if rand == 0:
			secondword = "Pass"
		elif rand == 1:
			secondword = "Meadow"
		elif rand == 2:
			secondword = "Hill"
		elif rand == 3:
			secondword = "Forest"
		else:
			secondword = "Haunt"
			
		self.name = firstword + " " + secondword	
		
	def print_info(self):
		print("NAME: " + self.name)
		print("Coordinates: %d,%d" %(self.x,self.y))
		print("-> people inside this Domain:")
		for i in range(0,len(self.majors_here)):
			print(self.majors_here[i].name)

	
	def draw_domains(self,dim):
		counter = dim*dim - dim + 1
		for k in range(dim):
			for i in range(dim):
				print("*-----",end="") #this just gets rid of that space at the end of the normal print
			print("*")
			for i in range(dim):
				if counter < 10:
					print("|  %d  "%(counter),end="")
				elif counter < 100:
					print("| %d  "%(counter),end="")
				else:
					print("| %d "%(counter),end="")
				
				if counter%dim == 0:
					counter = counter - (dim + (dim-1))
				else:
					counter += 1
	
			print("|")
		for i in range(dim):
			print("*-----",end="") #this just gets rid of that space at the end of the normal print
		print("*")
			
	#  *-----*-----*-----*
	#  |  1  |  2  |  3  |
	#  *-----*-----*-----*
		



			
			
			