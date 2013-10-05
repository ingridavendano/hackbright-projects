#!/bin/env python

s = """
Given a multiline string 's', print each line along with the line number

eg:
    mystr = "Sorry,\nMy people need me\nI must go"

    prints

    1. Sorry,
    2. My people need me
    3. I must go.

""" 


def print_str_number_lines(string):
	new_string = string.split("\n")

	for i in range(len(new_string)):
		print "%d. " % (i+1), new_string[i]


def main():
    mystr = "Sorry,\nMy people need me\nI must go"

    print_str_number_lines(mystr)


main()