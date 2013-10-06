#!/bin/env python

"""
Write a function with the following signature:
    title(str) -> str

It should take a string and capitalize it according to book title rules
    eg:
    title("a tale of two cities")
        => A Tale of Two Cities
"""


def title(my_title):
	if len(my_title) > 0:
		my_title[0].upper()

	print my_title
	words = my_title.split()
	capitalized_title = ""
	
	for word in words:
		if word not in ['of','to']:
			word = word[0].upper() + word[1:]
		capitalized_title += word + " "

	return capitalized_title


def main():
	string = "a tale of two cities"
	print title(string)


main()
