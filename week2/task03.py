#!/bin/env python

"""
Given list l1 and list l2, produce list l3 that contains the contents 
of both lists, removing duplicates
eg:
    l1 = [1,2,3]
    l2 = [2,3,4]
    
    l3 = [1,2,3,4]
"""


def combine_two_lists(list1,list2):
	new_list = list1 

	for item in list2:
		if item not in list1:
			new_list.append(item)

	return new_list


def main():
	l1 = [1, 3, 4, 6, 8, 10]
	l2 = [93, 2, 23, 77, 66]

	print l1
	print l2

	l3 = combine_two_lists(l1,l2)

	print l3
	

main()
