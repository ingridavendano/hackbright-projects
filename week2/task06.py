#!/bin/env python

"""
Given the string s, produce a list composed of all the single 
characters from the original string
eg:
    s = "Hello"
    becomes
    l = {"H", "e", "l", "l", "o"}
"""

def string_to_list(string):
	return [i for i in string]


def main():
	s = "Hi there, my name is Slim"
	print s

	s = string_to_list(s)
	print s


main()