import random


#Here we will throw whatever would have beaten our
#opponent last round

#Remember input has our opponents move from last round!

#in the first round input is empty!
if not input:
	output = random.choice(["R","P", "S"])

#for every turn but the first we go here	
else:

	#pick the move that beats twoBackThrow
	if *REPLACE* == "R":
		output = "P"

	elif *REPLACE* == "P":
		*REPLACE* = "S"
		
	elif input == "S":
		*REPLACE* = "R"

	