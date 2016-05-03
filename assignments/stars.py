# def draw_stars(a):

# 	for element in a:
# 		print element * ("*")



# draw_stars([4,6,1,3,5])


def draw_stars(a):

	for element in a:
		mylist = []
		firstLetter = ''
		#check type of element if it's a string then find the first letter
		if type(element) is str:
			#append the string to its own list then break up the list into elements
			mylist.append(element)
			#get the first letter of the new list and make it lowercase
			firstLetter = mylist[0][0].lower()
			#multiply the first letter by the length of the string
			lengthofelement = len(element)
			#multiply the first letter by the length of the string
			print firstLetter * lengthofelement
		# if it's a number
		else:
			print element * ("*")



draw_stars([4, "Tom", 1, "Michael", 5, 7])