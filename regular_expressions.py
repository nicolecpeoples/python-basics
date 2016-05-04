import re
"""
	Python re module provides regular expression support
	ex. match = re.search(pat, str)  pat = pattern  str = string

	****** Special Characters *****
	\ escape special characters
	. matches any character
	^ matches beginning of string
	$ matches end of string
	[5b-d] matches any chars '5', 'b', 'c' or 'd'
	[^a-c6] matches any char except 'a', 'b', 'c' or '6'
	R|S matches either regex R or regex S
	() creates a capture group and indicates precedence

	****** Special Sequences *****
	\A start of string
	\b matches empty string at word boundary (between \w and \W)
	\B matches empty string not at word boundary
	\d digit
	\D non-digit
	\s whitespace: [ \t\n\r\f\v]
	\S non-whitespace
	\w alphanumeric: [0-9a-zA-Z_]
	\W non-alphanumeric
	\Z end of string
	\g<id> matches a previously defined group



"""
str = 'an example word:cat!!'
match = re.search(r'word:\w\w\w', str) #r = raw string

if match:
	print 'found', match.group()
else:
	print 'did not find'