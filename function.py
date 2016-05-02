""" a function is a named flock of code that we can execute to perform a specific task

1. Acquire raw materials (variables) needed for creating a car.
2. Send the raw materials(invoke and pass arguments) to a car manufacturing plant (function)
3. Do something (process) with the raw materials(parameters) 
4. Drive the car (function's return value)

Functions are First Class functions and can go whereever they want.
	- standalone
	- defined inside classes/instances (known as methods)
	- passed as arguements to functions (callback)
	- returned from functions(creating a closure)
	- anonymous which are stored as variables/used only one time (lambdas)
"""

def add(a,b):
	x = a+b
	return x
	#the return value gets assigned to the "result" variable
result = add(3,5)
print result

def say_hi(name):
	print "hi, " + name

say_hi("nicole")
say_hi('charlie')
say_hi('kyle')

#returning values
def say_hi():
	return "hi"

greeting = say_hi()
print greeting