import random


#in the first round input is empty!
if not input:
	output = random.choice(["R","P", "S"])

#for every turn but the first we go here	
else:

	#pick the move that beats twoBackThrow
	if input == "R":
		output = "P"

	elif input == "P":
		output = "S"
		
	elif input == "S":
		output = "R"

	