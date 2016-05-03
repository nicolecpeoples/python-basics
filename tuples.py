""" A tuple is a container for a fixed sequence of data objects. The name comes from the Latin suffix for double, triple, quadruple, quintuple. Tuples are 
sequences, just like lists. The only difference is that tuples can't be changed and are immutable."""

tuple_data = ('phyiscs', 'chemistry', 1997, 2000)
tuple_num = (1,2,3,4,5)
typle_letters = ("a", "b", "c", "d")

""" tuples are useful for representing what other languages often call records -- some 
We can print the data from a tuple via an index. The index operator selects an element from a tuple """

julia = ("julia", "roberts", 1967, "duplicity", 2009, "actress", "atlanta, georgia")

#print julia[2]

# to print all the values inside a tuple, we can iterate through it using the loop



#slide a tuple
#julia = julia + ("eat pray love", 2010)

#[starting index: ending index]
julia = julia[:3] + ("eat pray love", 2010) + julia[5:]
#slice of after index three and before index five and replace with current values
for data in julia: 
	print data

#tuple packing
value = ("michael", "instructor", "coding dojo")
(name, position, company) = value #tuple unpacking
print name
print position
print company	


#value swapping the left side is a tuple of variables the right side is  a tuple of values
(a,b) = (b,a)

"""
Built in Tuple functions 

	len()
	max()
	min()
	sum()
	any()
	all() - returns true if all items are true
	enumerate()  - iterates through the tuple and returns two tuples (index, item)
	sorted() -returns a sorted list, not a tuple
	reversed() - iterate through the tuple in reverse order. the return value from reversed() is generic <reversed object>
	and must be fed into the tuple() or list() constructor to create one of those objects.

	
"""

#enumerate
num = (1,5,7,3,8)
#at whatever index, we will get the item for the tuple we are enumerating through
for index, item in enumerate(num):
	print(str(index)+" = " + str(item))


# Return Values
def get_circles_area(r):
	#return (circumfrance and area) of a circle of radius r
	c = 2 * math.pi * r
	a = math.pi * r * r
	return(c,a)
