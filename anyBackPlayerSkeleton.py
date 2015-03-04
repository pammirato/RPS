import random

turnsBack = 3

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

	#this stores the opponents last move in the history
	oldThrows.append(input)

	#len(oldThrows) == the number of rounds played
	#so if len(oldThrows) == 1, we have only played 1 round
	#and can't look two rounds back! just choose random
	if len(oldThrows) < *REPLACE*:
		output = random.choice(["R","P", "S"])

	#now we know we have played at least 2 rounds so far
	else:

		

		#get our opponets throw from 2 rounds back
		twoBackThrow = oldThrows[len(oldThrows)-*REPLACE*]

		#pick the move that beats twoBackThrow
		if twoBackThrow == "R":
			output = "P"

		elif twoBackThrow == "P":
			output = "S"
			
		elif twoBackThrow == "S":
			output = "R"

	