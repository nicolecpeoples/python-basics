#User Input
greeting = "Hello Ninja!"
print greeting
#you can use single or double quotes
print 'What is your name?'
#we use raw_input() to get user input and set it to a variable
name = raw_input()

print "How old are you?"
#we can also use input() to get user input
age = input()

#adding of variables to a string to be printed is like this:
print "Your name is", name
print "you are", age, "years old"

#you can also add the variable in between strings just like the above
raw_input("\n\nPress the enter key to exit.")
#the line above would make the app not close or exit out automatically