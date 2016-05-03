import random

head = 0;
tail = 0;
for count in range(1,10):
	random_num = round(random.random())

	if random_num == 0.0:
		side = "head"
		head +=1
	else:
		side = "tail"
		tail +=1
	
	print "Attempt #" , count, ": Throwing a coin... It's a", side, "Got ", head, "head(s) so far and ", tail, "tail(s) so far"

raw_input("\n\nEnding the program, thank you!")