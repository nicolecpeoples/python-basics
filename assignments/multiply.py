

# def multiply(a, b):
# 	for i in a: 
# 		i = (i *b)
# 		print i


# b = multiply([2,4,10,16], 5)
# print b


def multiply(a, b):
	for i in range(0, len(a)): 
		a[i] = (a[i] * b)
	return a


b = multiply([2,4,10,16], 5)
print b
