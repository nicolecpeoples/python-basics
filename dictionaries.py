""" 
 	- a dictionary is an unordered collection of objects
	- values are accessed using a key
	a dictionary can shrink or grow as needed
	- the contents can be modified
	- they can be nested
	- sequence operations such as slice can't be used
"""

weekend = { "Sun": "Sunday", "Mon": "Monday"} #literal notation
vals = dict(one = 1, two=2) #dict() function
capitals = {} #create an empty dictionary and add values
capitals["svk"] = "Bratislava"
capitals["deu"] = "Berlin"

d = { i:object() for i in range(4)} #dictionary comprehension

#to print all keys
for data in capitals:
     print data
#another way to print all keys
for key in capitals.iterkeys():
     print key
#to print the values
for val in capitals.itervalues():
     print val
#to print all keys and values
for key,data in capitals.items():
     print key, " = ", data

  """ Build in Dictionary functions 
  	cmp(dict1, dict2) - compares elements of both dictionaries
  	len() - length
  	str() produces a printable string representation
  	type() returns the type of the passed variable
  """
  """ Dictionary Methods 
  	.clear() - removes all elements from the dictionary
  	.copy() - returns a shallow copy dictionary
  	.fromkeys(sequence, [value]) - create a new dictionary with keys from sequence and values set to value
  	.get(key, default = none) - for key key returns value or default if key is not dictionary
  	.has_key(key) - returns true if a given key is available in the dictionary, otherwise false
  	.items() - returns a list of dictionary's (key, value) tuple pairs
  	.keys() - return a list of dictionary keys
  	.setdefault(key, default=none) - similar to get(), but will set dict[key] = default if key is not already in dictionary
  	.update(dict2) = adds dictionary dicts2 key-values pairs to an existing dictionary
  	.values() - returns list of dictionary values


  """

  #nesting is allowed and dictionaries may contain lists and tuples
  context = {
  	'questions': [
  		{ 'id': 1, 'content': 'why is there a light in the fridge and not in the freezer?'},
  		{ 'id': 2, 'content': 'Why don\t sheep shrink when it rains?'}

  	]
  }

  # to iterate the values, we can use the nested for loop
  for key, data in context.items():
  		for value in data:
  			print "Question #", value["id"], ":", value["content"]


#Lists from Dictionary

data ={ "house": "Haus", "cat": "Katze", "red": "rot"}

print data.items()
#[('house', 'Haus'), ('red', 'rot'), ('cat', 'Katze')]
print data.keys()
# [ house, cat, red]

print data.values()
#[Haus, rot, katze]

#dictionaries from lists using the function zip()
dishes = ["pizza", "sauerkraut", "paella", "hamburger"]
countries = ["italy", "germany", "spain", "usa"]

country_specialties = zip(countries, dishes)

#it can now be transformed into a dictionary with dict()
country_specialties_dict = dict(country_specialties)




