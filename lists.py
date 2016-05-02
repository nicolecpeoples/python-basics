#a list, also known as an array is a data taype that allows you to hold groups of values.

ninja = ['rozen', 'kb', 'oliver']
my_list = ['4', ['list', 'in', 'a', 'list'], 987]

fruits = ['apple', 'banana', 'orange', 'strawberry']
vegetables = ['lettuce', 'cucumber', 'carrots']

fruits_and_vegetables = fruits + vegetables
print fruits_and_vegetables

#manipulating lists

"""
.append()
.remove()	-removes actual value, can error if it doesn't exist
.insert()
.pop() - remove the item at a given position; if the position is not given it will remove from the last entry.
.sort() - sorts the elements in a list

slicing using [] characters to return a copy of the list, constrained to specific indices. the starting index and ending index should be separated by the ":" character.

.len() returns number of items in a sequence
.max() returns max
.min() returns min

all() returns true if all items in the seq are true
"""
x = [1,2,3,4,5]
y = [10,11,12,13,14]
#x.append(99)
#x.insert(4, 99)
x.pop()
y.pop(1)

print x
print y