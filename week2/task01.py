#!/bin/env python

"""
Given list l, sort it in reverse order
ie: 10, 9, 8, 7, 6
"""


def reverse(l):
	for i in range(len(l)/2):
		tmp = l[i]
		l[i] = l[-i-1]
		l[-i-1] = tmp

	return l


def main():
	l = [5,2,1,5,9,10,11]

	print "Before:",l
	reverse(l)
	print "After:",l


main()
