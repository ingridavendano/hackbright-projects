#!/bin/env python

"""
Given the string s, excise characters 6 through 12, inclusive
eg:
    s = "Hello, good sir"
    becomes 
    s = "Hello sir"
"""


def remove_6_to_12(string):
	string = string[:5] + string[11:]
	return string


def main():
	# s = "Hi there, my name is Slim"
	s = "Hello, good sir"

	s = remove_6_to_12(s)
	print s


main()
