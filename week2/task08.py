#!/bin/env python

"""
Given two dictionaries, d1 and d2, update the contents of d1 
with the contents of d2, overwriting any existing keys
eg:
    d1 = {"a":1, "b":2}
    d2 = {"a":3, "c":4}

    becomes

    d1 = {"a":3, "b":2, "c":4}
"""


def combine_two_dicts(d1,d2):
	d3 = d1

	for key,value in d2.iteritems():
		d3[key] = value


	return d3


def main():
	d1 = {"a": 5, "c": 7, "d": 9, "q": 15}
	d2 = {"a": 6, "e": 13, "g": 6, "q": 1}

	d3 = combine_two_dicts(d1,d2)
	print d3


main()