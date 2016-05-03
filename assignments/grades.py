
count=10

while count > 0:

	print "What is your grade?"
	grade = raw_input()

	if grade >= "90":
		print "Score: " , grade, "; Your grade is a A" 
	elif grade >= "80":
		print "Score: " , grade, "; Your grade is a B" 
	elif grade >= "70":
		print "Score: " , grade, "; Your grade is a C"
	elif grade >= "60":
		print "Score: " , grade, "; Your grade is a D" 
	else:
		print "You've failed, I'm sorry :("
	

	count -=1


raw_input("\n\nEnd of Program. Bye!")