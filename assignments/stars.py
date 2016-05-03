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
			#
			mylist.append(element)
			firstLetter = mylist[0][0].lower()
			lengthofelement = len(element)

			print firstLetter * lengthofelement
		# if it's a number
		else:
			print element * ("*")



draw_stars([4, "Tom", 1, "Michael", 5, 7])