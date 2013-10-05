#!/bin/env python

"""
Given the string s, split it into two strings, s2 and s3, s2 
containing the first 5 letters of the string, and s3 containing 
the remaining letters.

eg:
    s1 = "Hello there"
    s2 = "Hello"
    s3 = " there"

"""


def split_str_in_two(string):
	return string[:5], string[5:]


def main():
	s = "Hi there, my name is Slim"
	s2,s3 = split_str_in_two(s)

	print s2
	print s3
	

main()
