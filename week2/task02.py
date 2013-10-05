#!/bin/env python

"""
Given dictionary d, print out the key-value pairs in alphabetical 
order by key, separated by commas
eg:
a, 1
b, 2
c, 4
d, 6
"""


def print_key_value_pairs(dictionary):
	for key,value in dictionary.iteritems():
		print key + ",", value


def main():
	d = {"q": 5, "m": 3, "z":2, "a": 10}

	print d
	print_key_value_pairs(d)


main()
