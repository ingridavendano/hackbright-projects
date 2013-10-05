#!/bin/env python

"""
Given the list l composed of tuples, sort the list by the second 
item in the tuple
    l = [(1,3), (3,2), (5,1)]
    becomes
    l = [(5,1), (3,2), (1,3)]
"""


def sort_by_second_typle_item(l,index):
	if index < len(l):
		for i in range(index,len(l)):
			if l[index][1] > l[i][1]:
				tmp = l[i]
				l[i] = l[index]
				l[index] = tmp

		sort_by_second_typle_item(l,index+1)

	return l


def main():
	l = [(1,2), (3,1), (17, 35), (81,20)]
	print sort_by_second_typle_item(l,0)


main()
