# Designing and debugging - coding up my own game

"""
To-Do:
- Make nope() exit back to previous method
"""

from sys import exit

global looked_left
looked_left = 0
global looked_right
looked_right = 0
global inquisitive
inquisitive = 0

def look_right():
	print "You look further up the road."
	print "You see a charming row of houses with neat gardens."
	
	looked_right = 1
	start_again()

def look_left():
	print "You look back up the road."
	print "You see the trail of breadcrumbs that lead you here."
	
	looked_left = 1
	start_again()

def start_again():
	print looked_left
	print looked_right
	if looked_left == 1 and looked_right == 1:
		print "You are an inquisitive one!"
		print "You got Inquisitive +1!"
		inquisitive = 1
	print "You refocus on the door in front of you."
	print "Do you open the door, look left, or look right?"
	
	next = raw_input("> ")
	if "open" in next:
		hallway()
	elif "left" in next:
		look_left()
	elif "right" in next:
		look_right()
	else:
		nope()
	
def nope():
	print "Nope! That's not valid. Start again to teach you a lesson!"
	exit(0)

def start():
	print "You are on a cul-de-sac in front of a newly built house."
	print "It is a sunny day and the house has a beautiful frontage."
	print "For some reason though, you don't feel quite right..."
	print "Do you open the door, look left, or look right?"
	
	next = raw_input("> ")
	if "open" in next:
		hallway()
	elif "left" in next:
		look_left()
	elif "right" in next:
		look_right()
	else:
		nope()
		
start()