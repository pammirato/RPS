import random

roundsBack = 3

#Here we stores all the moves of the opponent
#in a list called oldThrows

#We then make our throw (output) to be whatever
#would have beaten our oponent in two rounds back

#the goal is just to see how to store history 


#in the first round input is empty!
if not input:
	#so initialize the list, and pick a random throw
	oldThrows = []
	output = random.choice(["R","P", "S"])

#for every turn but the first we go here	
else:
	#len(oldThrows) == the number of rounds played
	#and we need to have played at least as many rounds
	#as we want to look back.
	if len(oldThrows) < *REPLACE*:
		output = random.choice(["R","P", "S"])

	#now we know we have played at least 2 rounds so far
	else:

		#get our opponets throw from 2 rounds back
		anyBackThrow = oldThrows[len(oldThrows)- *REPLACE*]

		#pick the move that beats twoBackThrow
		if *REPLACE* == "R":
			output = "P"

		elif *REPLACE* == "P":
			output = "S"
			
		elif *REPLACE* == "S":
			output = "R"

	oldThrows.append(*REPLACE*)