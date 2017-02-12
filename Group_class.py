from __future__ import print_function
from random import randint


class Group:
	
	def __init__(self,leader): #instance variables unique to each instance
		self.leader = leader
		self.members = [leader]  #includes leader
		
		self.name = "Anonymous" 
		
		self.currentdomain = None
		
		
	def join(self,member):
		self.members.append(member)
		
	def remove_member(self,member):
		self.members.remove(member)
		
	def depose(self):
		self.leader = None
		
	def new_leader(self,newleader):
		self.leader = newleader
		
	def size_of_group(self):
		len(self.members) + 1
		
	
		
	
		
		
		