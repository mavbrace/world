#this program will generate people over time...

import copy
from random import randint   #how to: randint(0,9)

from Person_class import Major, Normal
from Scene_class import Scenario
from Domain_class import Domain
from Group_class import Group


def stage(scenes,majors,stage_num,fem_names,male_names,domains):
			
	#run through each Major, going through the specific scenario they're in
	where_in_list = 0
	for person in majors:
	
		acquired_a_partner = False
	
		random_scenario_index = randint(0,len(scenes)-1)
		scene = scenes[random_scenario_index]
				
		if person.state == "alive" and person.age > 12:
		
			#---PARTNERSHIP!!---#
			if random_scenario_index == 0 and person.partner == None:
				acquired_a_partner = partnership(person,majors,where_in_list)						
																					
			#---MURDER!!---#
			elif random_scenario_index == 1 and person.age > 12:
				murder(person,majors,where_in_list,scenes,random_scenario_index,stage_num)						
										
			#---TREASURE!!---#
			elif random_scenario_index == 2:
				treasure(person)
									
			#---KID!!---#
			elif random_scenario_index == 3:
				kid(person,fem_names,male_names,majors)
				
			#---FIGHT SOMETHING!!---#
			elif random_scenario_index == 4:
				fight(person)
				
			#---FORM A GROUP!!---#  
			elif random_scenario_index == 5:
				group(person)
		
		
			#just in case... they died...
			if person.state == "dead":
				return
											
			#Now, after all those if statements, we continue with some...
			#--------OTHER POSSIBLE THINGS THAT MIGHT HAPPEN-------------#
			
			#someone might [[ Leave Their Partner ]]
			#later add: it's harder to leave if they're in love, much easier if just business partners, and loyalty!
			#(only if they didn't get a partner THIS stage)
			if not acquired_a_partner:
				leave_chance = randint(0,2^person.loyalty)
				if (leave_chance == 2 and 
				person.partner != None and 
				person.partner.state == "alive"
				):
					person.old_partners.append(person.partner)
					person.partner.old_partners.append(person)
					temp = person.partner
					person.partner = None
					temp.partner = None
					person.loyalty == 0
					temp.loyalty = temp.loyalty/2
			
				#you didn't leave your partner, therefore your loyalty goes up 1! Yay!
				#also, loyalty maxes out at 20 (that's about 1 in a million for the leave_chance)
				if (
				len(person.old_partners) == 0 and 
				person.partner != None and 
				person.partner.state == "alive" and
				person.loyalty <= 20
				):
					person.loyalty += 1
			
			
			#   [[[ CHANGE DOMAINS ]]]   #	
			#first, delete person from their old domain (MAJORS_HERE) (added at the beginning of this stage)
			if person in person.current_domain.majors_here:
				person.current_domain.majors_here.remove(person)			
			#--[[The person moves to a new domain]] - or not (later)
			goto_new_domain(domains,person)			
			
			
				
			#------------------------DONE--------------------------------#		
						
		where_in_list += 1
	

def fight(person):
	opponent = ""
	opponent_strength = 0
	if len(person.current_domain.creatures) < 1:
		return
	random_opponent_index = randint(0,len(person.current_domain.creatures)-1)
	opponent = person.current_domain.creatures[random_opponent_index]

		
	luck = randint(0,4)
	
	if luck + person.strength >= opponent["Danger Level"]:
		person.strength += 1
		person.defeated_opponents.append(opponent["Name-Singular"])
	
			
						
def partnership(person,majors,where_in_list):

	acquired_a_partner = False

	#grab somebody as a partner (romantic or not, doesn't matter)
	#only searches people who are currently in the same domain as you
	
	nearby_majors = person.current_domain.majors_here #just so we don't have to keep typing this over and over!!
	
	#if you're the only one there
	if len(nearby_majors) <= 1:
		return False
	random_partner_index = randint(0,len(nearby_majors) - 1)
	# if you try to become a partner with yourself, increase index by 1
	#or if you try to become a partner with your kid
	count = 0
	
	while nearby_majors[random_partner_index].uniqueID == person.uniqueID or nearby_majors[random_partner_index] in person.kids:
		if count > len(majors):
			return False #we looked through all the people, and there's nobody suitable as a partner
			#thus broken out of this function (partnership)
	
		random_partner_index = (random_partner_index + 1) % len(nearby_majors)
		count += 1
		 

	partner = nearby_majors[random_partner_index]
	
	
	#--SUCCESS!--#
	if partner.partner == None and partner.state == "alive" and partner.age > 12 and person.age > 12:			
		person.partner = partner	
		partner.partner = person
		
		#print(person.name + " has partnered with " + partner.name)
		
		acquired_a_partner = True
		
		#decide what relationship they have (soulmates,lovers,friends,business)
		random_relationship = randint(0,40)
		if person.gender != person.partner.gender:
			#--SOULMATE--# (1/40)
			if random_relationship == 0:
				person.relationship = "soulmate"
				person.partner.relationship = "soulmate"
				person.loyalty = 20;
				person.partner.loyalty = 20;
			#--BUSINESS--# (7/40)
			elif random_relationship > 0 and random_relationship < 8:
				person.relationship = "business"
				person.partner.relationship = "business"
				person.loyalty = 1;
				person.partner.loyalty = 1;
			#--FRIENDS--# (12/40)
			elif random_relationship > 7 and random_relationship < 20:
				person.relationship = "friends"
				person.partner.relationship = "friends"
				person.loyalty = 1;
				person.partner.loyalty = 1;
			#--LOVERS--# (20/40)
			else:
				person.relationship = "lovers"
				person.partner.relationship = "lovers"
				person.loyalty = 2;
				person.partner.loyalty = 2;
										
		else:
			#--SOULMATE--# (1/40)
			if random_relationship == 0:
				person.relationship = "soulmate"
				person.partner.relationship = "soulmate"
				person.loyalty = 20;
				person.partner.loyalty = 20;
			#--BUSINESS--# (14/40)
			elif random_relationship > 0 and random_relationship < 15:
				person.relationship = "business"
				person.partner.relationship = "business"
				person.loyalty = 1;
				person.partner.loyalty = 1;
			#--FRIENDS--# (20/40)
			elif random_relationship > 14 and random_relationship < 36:
				person.relationship = "friends"
				person.partner.relationship = "friends"
				person.loyalty = 1;
				person.partner.loyalty = 1;
			#--LOVERS--# (5/40)
			else:
				person.relationship = "lovers"
				person.partner.relationship = "lovers"
				person.loyalty = 1;
				person.partner.loyalty = 1;		
		
	return acquired_a_partner		



def murder(person,majors,where_in_list,scenes,random_scenario_index,stage_num):

	#better chance to kill again if they've killed before, recently
	#check every 10 stages (temp)				
	if person.stages_lived_through % 10 == 0 and len(person.people_killed) > 2:
		chance = 11 #50% chance				
	elif person.stages_lived_through < 5:
		chance = 6 #25% chance
	else: #don't murder anybody(probably)
		chance = 1
		
	
	random_murder = randint(0,20) 
	if random_murder < chance:

		nearby_majors = person.current_domain.majors_here #just so we don't have to keep typing this over and over!!
		random_kill_index = randint(0,len(nearby_majors) - 1)
		#well it ain't suicide, and let's not kill any kids (skipping over the people in the array until suitable victim found)
		#and you can't kill your own kid
		count = 0
		while (
		random_kill_index == where_in_list or 
		nearby_majors[random_kill_index].age < 13 or 
		nearby_majors[random_kill_index] in person.kids
		):
			#so that the loop won't accidentally go on forever:
			if count > len(majors):
				return  #will make do for now!
				
			random_kill_index = (random_kill_index + 1) % len(nearby_majors)
			count += 1
		

		killed_person = nearby_majors[random_kill_index]
		
		#person.people_killed.append(killed_person)
		

		#-----------MESSAGE-------------------#
		'''
		if person.partner == killed_person:
			print(person.name + " has killed their partner, " + killed_person.name + "!")
		else:
			print(person.name + " has killed " + killed_person.name  + "!\n->Murder number %d" %(len(person.people_killed)))
		'''
		#-----------END OF MESSAGE------------#
		
		reasons_why = scenes[random_scenario_index].reasons_why
		random_reason = randint(0,len(reasons_why)-1)		
		
		#print("The reason: " + reasons_why[random_reason])
		
		#The murderer's information if updated:
		person.murder(killed_person,killed_person.pocket)				
		#The murdered person DIES HERE:
		killed_person.die(person,random_reason,stage_num,True)

					
		#----REVENGE-----#
		#now there's a chance that, if the person killed had a partner who's alive, then that partner comes and gets revenge
		#they don't take the person's stuff, in this case
		random_revenge = randint(0,1)
		if random_revenge == 0 and killed_person.partner != None and killed_person.partner != person:
			if killed_person.partner.state == "alive":
				#print(killed_person.partner.name + " has taken revenge for the death of their partner. " + person.name + " is now dead.")
				
				#The murderer's info is updated:
				killed_person.partner.murder(person,[])								
				#person DIES HERE:
				person.die(killed_person.partner,"Revenge",stage_num,False)									



def treasure(person):

	if len(person.current_domain.treasure) < 1:
		return
	what_object = randint(0,len(person.current_domain.treasure)-1)
	
	person.pocket.append(person.current_domain.treasure[what_object])

	#just a temp thing..
	if what_object == 9:
		person.strength += 1  #gives you strength



def kid(person,fem_names,male_names,majors):
	#Now, the conditions are: you must have a partner of the opposite gender, 
	#both over 18 and under 51, and alive, and not have more than 6 kids already			
	if (
	person.partner != None and 
	person.gender != person.partner.gender and 
	person.age > 18 and person.partner.age > 18 and 
	person.age < 51 and person.partner.age < 51 and
	person.partner.state == "alive" and
	len(person.kids) <= 6
	): 
		random_gender = randint(0,1)
		gender = ""
		
		
		if random_gender == 0:
			gender = "female"
			random_name = randint(0,len(fem_names)-1)
			name = fem_names[random_name]
		else:
			gender = "male"
			random_name = randint(0,len(male_names)-1)
			name = male_names[random_name]
			
		#--CREATE THE KID!--#
		kid = Major(0,name,gender,Major.nextID)
		Major.nextID += 1
		
		kid.current_domain = person.current_domain
		kid.current_domain_index = person.current_domain_index
		kid.current_domain.majors_here.append(kid)
		
		majors.append(kid)
		
		Major.number_of_majors += 1
		
		#------------MESSAGE-----------#
		#print(person.name + " and " + person.partner.name + " have had a kid named " + kid.name)
		#--------------END-------------#
		
		person.kids.append(kid)
		person.partner.kids.append(kid) 
		kid.parents[0] = person
		kid.parents[1] = person.partner
		kid.domain_born_in = kid.current_domain
		
		
def group(person):
	
	#search people in same domain as you: if any of them have an existing group, join it.
	#if there are no existing groups, make your own. Be the leader of said group.
	#ALSO if you're really AMBITIOUS you might form a group, but get your members later!
	#later, if your influence is greater than the leader you may overthrow/peacefully replace them.
	
	
	#you're a real ambitious person, eh... make your own group, but no members yet
	if person.ambition > 10 and person.group == None:
		newgroup = Group(person)
		newgroup.name = person.name + "'s Group"
		person.group = newgroup #adding link to group from person
		return
	
	#search the people in the domain...
	for other in person.current_domain.majors_here:
				
		#if you already have a group you can add another member....  //TODO
		if person.group != None and other.group == None:
			person.group.join(other)
				
		#join a group if there's one nearby (as long as you're not part of another group)
		if other.group != None and person.group == None:
			other.group.join(person)
			person.group = other.group  #adding link to group from person
			return
			
	#make your own group
	if len(person.current_domain.majors_here) > 1:	
		rand = randint(0,len(person.current_domain.majors_here)-1)
		#make sure you don't form a group with yourself (because that's just sad)
		#and don't add someone who's already in a group(not yet anyway)
		if person.current_domain.majors_here[rand] != person and person.current_domain.majors_here[rand].group == None:
			random_person = person.current_domain.majors_here[rand]
			newgroup = Group(person)
			newgroup.join(random_person)
			newgroup.name = person.name + "'s Group"
			person.group  = newgroup
			return
				
		
	
	
	
	
		
#each year this is called; all the majors have already been gone through in stage()
#HEREIN we age the people, or they die of old age
def finalize_stage(majors,stage_num):
		#run through each Major and Normal, increasing their age by 1
		#as well as increasing their 'stages lived through' amount by 1
		#then a chance they die if they're too old
	for person in majors:
		if person.state == "alive":		
			if person.age > 80:
				chance_to_die = randint(0,10)
				#they die of old age:
				if chance_to_die == 6:
					person.die(None,"Old Age",stage_num,False)
					#print("==>" + person.name + " has died of old age! <==")
				else:
					person.age += 1
					person.stages_lived_through += 1
			else:
				person.age += 1
				person.stages_lived_through += 1
					

#go through majors, check if any are left alive
def check_if_any_alive(majors):
	yes = False
	for person in majors:
		if person.state == "alive":
			yes = True
			
	return yes
		
	

def make_domains(dimensions):
	Domain.dimensions = dimensions  #ie width x height -- and it's a square
	
	domains = []
	danger = randint(0,10)
	wealth = randint(0,10)
	count = 1
	#x and y
	#each domain has certain characteristics
	for y in range(0,dimensions):
		for x in range(0,dimensions):
			domains.append(Domain(x,y,danger,count))
			count+=1
			
	for domain in domains:
		#now add some creatures/dangers to the domain (more types if more danger)
		for blah in range(0,danger):
			rand = randint(0,Domain.number_of_possible_creatures-1)
			domain.add_creature(rand)
			
		#and some treasure (more types if more wealth)
		for blah in range(0,wealth):
			rand = randint(0,Domain.number_of_dif_treasures - 1)
			domain.add_treasure(rand)
			
		#update the name of the domain:
		domain.update_name()
		#print domain.name
		
	return domains
			
		
			
def goto_new_domain(domains,person):

	limit = 50  #just in case - so the while loop doesn't go forever if there's a glitch
	addto_x = 0
	addto_y = 0
	new_x = 0
	new_y = 0
	go = True
	
	while go:
		#randomly go to a new domain
		rand = randint(0,3)
		if rand == 0: #go to the East
			addto_x = 1
		elif rand == 1: #go to the West
			addto_x = -1
		elif rand == 2: #go to the North
			addto_y = 1
		elif rand == 3: #go to the South
			addto_y = -1
		
		new_x = person.current_domain.x + addto_x
		new_y = person.current_domain.y + addto_y
		
		
		dim = Domain.dimensions
		#now check if they went out of bounds
		if new_x < 0 or new_x > (dim-1) or new_y < 0 or new_y > (dim-1):
			go = True
		else: #otherwise, break free from the loop
			go = False
			
		
	#sorry about this line - convert_to_domain just takes the x,y coordinates and finds the domain that they belong to
	index = convert_to_domain_index(new_x,new_y)
	person.current_domain = domains[index]
	person.current_domain_index = index
	domains[index].majors_here.append(person)
	
	
		
#I go from the bottom left, x values increasing first (left across) then 
#skip up (+y) to the next row, from the left to the right, etc.
#The array of domains is ordered this way
#|--->|
#|--->| ^
#|--->| ^
def convert_to_domain_index(x,y):
	#my super-cool (and probably unnecessary) equation
	return (x + (y*Domain.dimensions))
	
	

def main():
	#load in male and female names from text files: malenames.txt, femalenames.txt
	namefile_female = open('femalenames.txt',"r")
	namefile_male = open('malenames.txt',"r")
	
	female_names = namefile_female.read().split(',')
	
	male_names = namefile_male.read().split(',')	
	
	
	#----ADD DOMAINS----#
	DIMENSIONS = 4  #--must be over 1!
	domains = make_domains(DIMENSIONS)
	
		
	majors = []
	normals = []
	#change to dictionary later - but Aidan says there's nothing wrong with it, so maybe not
	names = ["Sam","Bob","Carl","Susan","Lucy","Kally","Swift"]
	genders = ["male","male","male","female","female","female","male"]
	
	#FIVE majors at the start (currently)-- or, uh, six?
	for i in range (0,5):
		majors.append(Major(19,names[i],genders[i],Major.nextID)) # nextID is the unique ID of the person. Starts at 0.
		Major.nextID += 1
		Major.number_of_majors += 1
		majors[i].current_domain = domains[0]
		domains[0].majors_here.append(majors[i])
		majors[i].domain_born_in = domains[0]
		
		
	#normals(25 currently)	 -- spread them out over the domains	
	for i in range(0,25):
		random_age = randint(12,60)
		rand_gender = randint(0,1)
		if rand_gender == 0:
			random_gender = "female"
		else:
			random_gender = "male"
		normals.append(Normal(random_age,"Normal",random_gender))
	
	
	
	#----populate the Available Scenarios (pre-made)----#
	scenes = []
	scenes.append(Scenario("Become Partners With Somebody",1))
	
	scenes.append(Scenario("Kill Somebody",4))
	scenes[1].reasons_why = ["None Given","Really Disliked Their Haircut","Horrible Accident","Jealousy","Snide Remarks Made","Threatened"]
	
	scenes.append(Scenario("Look For Treasure",3))
	scenes.append(Scenario("Have a Kid",5))
	scenes.append(Scenario("Fight Something",6))
	scenes.append(Scenario("Join a Group",7))
	
	
		
		
	#now continuously run through stages...
	#testing just a few times
	#-------~~~~~***| THIS IS THE MAIN SCENARIO |***~~~~~~---------#
	stage_num = 0 #ie 'year'
	
	annihilation = False
			
	sim_length = int(raw_input("How many years would you like to run the simulation? ")) #ie number of stages or 'years'
	loop = raw_input("Would you like to loop until people survive? (y/n) WARNING could be slow!!")
	
	original_majors = copy.deepcopy(majors)
	
	while(True):
		majors = copy.deepcopy(original_majors)
		
		annihilation = False
		stage_num = 0
		for i in range(0,sim_length):
			stage(scenes,majors,stage_num,female_names,male_names,domains)
			finalize_stage(majors,stage_num)
			stage_num += 1
		
			any_survivors = check_if_any_alive(majors)
			if not any_survivors:
				annihilation = True
				break
					
		if loop == 'n' or annihilation == False:
			break
			
		
		
	if annihilation:
		print("......There is nobody left alive.....")
	else:
		print("-----People Alive:------")
	
		for peep in majors:
			peep.cleanup()
			if peep.state == "alive":
				peep.print_information()
			elif peep.state == "deceased":
				print("-> DEAD <-")
	

	#~~~at end draw domains~~~#
	domains[0].draw_domains(DIMENSIONS)
	asker = True

	while asker:
		answer = raw_input(">Press 1 to open INFORMATION of one of the domains above \n>Press 2 to open a person's family tree \n>Press 'n' to quit\n...")
		if answer == "n":
			break
		elif answer == "2":
			id = int(raw_input("Please enter their ID number --> "))
			if id > Major.nextID:
				print("Sorry, invalid ID...")
			else:
				print(len(majors)) ##---PRINT STATEMENT---##
				#for some reason this goes out of range(id) when the sim runs over about 100 years...?
				familytreePerson = majors[id]
				familytreePerson.print_familytree()
			
		else:
			region = int(raw_input("Okay. Please enter the number of the region you'd like to access: "))
			if region > 0 and region <= DIMENSIONS*DIMENSIONS:
				domains[region-1].print_info()
			else:
				print("Sorry, the region you entered is out of bounds.")
	
	
	
	#-------~~~~~~~~~~~~~***|    END    |***~~~~~~~~~~~~~--------#
		
		
	
	
	
if __name__ == "__main__": main()