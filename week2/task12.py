#!/bin/env python

"""
Write the following two functions
    c_to_f(float) -> float
    f_to_c(float) -> float

c_to_f should convert a temperature in celsius to fahrenheit, 
and f_to_c should do the opposite
"""


def c_to_f(number): 
	return (9/5. * number) + 32. 


def f_to_c(number):
	return 5/9. * (number - 32.)


def main():
	temp_in_c = 25.		# C
	temp_in_f = 82.		# F

	print "%d C --> %d F" % (temp_in_c,c_to_f(temp_in_c))
	print "%d F --> %d C" % (temp_in_f,f_to_c(temp_in_f))


main()
