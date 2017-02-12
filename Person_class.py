from __future__ import print_function

class Major:

	number_of_majors = 0  # class variable shared by all instances
	number_of_dead_majors = 0
	nextID = 0
	
	def __init__(self,age,name,gender,uniqueID): #instance variables unique to each instance
		self.age = age
		self.name = name
		self.gender = gender
		
		self.uniqueID = uniqueID
		
		self.strength = 0 #from 0 to 100, OVERALL STRENGTH, physical strength + skill + whatever else
		self.defeated_opponents = []
		self.number_of_each_opponent = []
		
		self.social = "" #options: loner,non-intimate,....uh
		#the more you leave your partners, the more anti-social you become, I guess
		#though you might start out like that, but not a great chance for that!
		
		self.partner = None
		self.relationship = "" #options: soulmates,lovers,friends,business
		self.loyalty = 0 #the level of loyalty person has to their partner. Makes it harder to leave them.
		#also should make it more likely they will seek revenge if their partner is killed. 
		#Loyalty maxes out at 21 (2^20 = about a million)
		self.old_partners = []
		
		self.people_killed = []  #add a link to a dead person!
		
		self.pocket = [] #names of objects found
		self.number_of_each_item = [] #for duplicates (filled in by calling cleanup() below)
		
		self.stages_lived_through = 0
		
		self.kids = []
		
		self.parents = [None,None]
		
		self.state = "alive" #--or deceased
		self.murdered_by = None
		self.reason_dead = ""
		self.date_died = -1
		
		self.current_domain = None  #link to the Domain they're currently in
		self.current_domain_index = 0 #careful - if I change the fact that they all start at 0,0, then this'll have to change
		self.domain_born_in = None
		
		self.group = None
		self.ambition = 0  #ambition affects how much you want to LEAD, but not necessarily your ability to do so
		
		
	def die(self,murdered_by,reason,date,is_stuff_taken):
		self.state = "deceased"
		self.murdered_by = murdered_by
		self.reason_dead = reason
		self.date_died = date
		
		if self in self.current_domain.majors_here:
			self.current_domain.majors_here.remove(self)
		
		Major.number_of_dead_majors += 1
		
		if is_stuff_taken:
			self.pocket = []
		
	def murder(self,person_killed,stuff_taken):
		self.people_killed.append(person_killed)
		self.pocket += stuff_taken
			
		
	def cleanup(self):
		#clean all the stuff up, make it more sensible 
		
		new_list = []
		number_of_each_list = [] #should be the same length as new_list list
		num = 0
		
		#clean up the person's pockets
		for item in self.pocket:
			#remove all the instances of item in the list!
			while item in self.pocket:
				self.pocket.remove(item) 
				num += 1
			number_of_each_list.append(num)
			new_list.append(item)
			num = 0
			
		self.pocket = new_list
		self.number_of_each_item = number_of_each_list
		num = 0
		new_list = []
		number_of_each_list = []
			
		#clean up the opponents they've defeated
		for opp in self.defeated_opponents:
			while opp in self.defeated_opponents:
				self.defeated_opponents.remove(opp) 
				num += 1
			number_of_each_list.append(num)
			new_list.append(opp)
			num = 0
			
		self.defeated_opponents = new_list
		self.number_of_each_opponent = number_of_each_list
				
						
			
	def print_information(self):
	
		print("--> " + self.name)
		
		if self.partner != None:
			print(self.name + "'s Partner: " + self.partner.name)
			print("Their relationship: " + self.relationship)
			print("Level of loyalty: %d" %self.loyalty)
			
		if len(self.old_partners) > 0:
			print("Has had %d old partner(s)." %len(self.old_partners))
			
		if len(self.kids) > 0:
			print("Kids: [%d]" %len(self.kids))
			for kid in self.kids:
				print(kid.name)
			
		print( "Number of people killed: %d" % len(self.people_killed))
		if len(self.people_killed) > 0:
			for peep in self.people_killed:
				if peep.reason_dead == "Revenge":
					print("One of " + self.name + "'s old partners was killed by " + peep.name + ", so " + self.name + " sought revenge.")
		
		print("Stuff in pockets:")
		for i in range(0,len(self.pocket)-1):
			print("%s  [amount: %d]" %(self.pocket[i],self.number_of_each_item[i]))
			
		print("Strength: %d" %self.strength)
		print("Defeated Opponents:")
		for i in range(0,len(self.defeated_opponents)-1):
			print("%s  [number: %d]" %(self.defeated_opponents[i],self.number_of_each_opponent[i]))
			
		print("-> they are currently in Domain #%d and they were born in Domain #%d" %((self.current_domain_index+1),self.domain_born_in.domain_num))
				
		if self.group != None:
			print("  [They are in the group: " + self.group.name + "]")
			print("Members: ",end="")
			for member in self.group.members:
				print(member.name,end="")
				if member.state == "deceased":
					print("(d)",end="")
				print("..",end="")
				
			print("")
	
		print("Age: %d" %self.age) #is this right? Seems weird sometimes.
		
		print("---[ ID: %d  ]---" %self.uniqueID)
		
		
		print("=============")


		
	# Function to  print level order traversal of tree
	def print_familytree(self):
		ancestors = []
		if len(self.parents) < 2:
			print ("     |      ")
			print (self.name)
			return


		currentLevel = []
		nextLevel = []
		currentLevel.append(self)
		while len(currentLevel) > 0:
			currentNode = currentLevel[0]
			del currentLevel[0]
			if currentNode != None:
				print(currentNode.name + " ",end="")
				nextLevel.append(currentNode.parents[0])
				nextLevel.append(currentNode.parents[1])
			if len(currentLevel) == 0:
				print("\n    -----     ")
				temp = currentLevel
				currentLevel = nextLevel
				nextLevel = temp
 




#------------------------------------------------------------------------#
#-------------------------------Normals----------------------------------#
#------------------------------------------------------------------------#		
class Normal:

	number_of_normals = 0
	number_of_dead_normals = 0

	def __init__(self,age,name,gender):
		self.age = age
		self.name = name
		self.gender = gender	
		
		self.state = "alive"
		
	
		
		
		
		
		
		
		
		
		
		
