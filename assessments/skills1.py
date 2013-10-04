# Things you should be able to do.

# Write a function that takes a list and returns a new list with only 
# the odd numbers.
def all_odd(some_list):
	new_list = []

	for i in range(len(some_list)):
		if some_list[i] % 2 == 1:
			new_list.append(some_list[i])

	return new_list

# Write a function that takes a list and returns a new list with only
# the even numbers.
def all_even(some_list):
	new_list = []

	for i in range(len(some_list)):
		if some_list[i] % 2 == 0:
			new_list.append(some_list[i])

	return new_list

# Write a function that takes a list of strings and returns a new list 
# with all strings of length 4 or greater.
def long_words(word_list):
	new_list = []

	for i in range(len(word_list)):
		if len(word_list[i]) >= 4:
			new_list.append(word_list[i])

	return new_list

# Write a function that finds the smallest element in a list of 
# integers and returns it.
def smallest(some_list):
	if len(some_list) == 0:
		return None

	smallest_int = some_list[0]

	for i in range(len(some_list)):
		if some_list[i] < smallest_int:
			smallest_int = some_list[i]

	return smallest_int

# Write a function that finds the largest element in a list of 
# integers and returns it.
def largest(some_list):
	if len(some_list) == 0:
	    return None

	largest_int = some_list[0]

	for i in range(len(some_list)):
		if some_list[i] > largest_int:
			largest_int = some_list[i]

	return largest_int

# Write a function that takes a list of numbers and returns a 
# new list of all those numbers divided by two.
def halvesies(some_list):
	new_list = []
	for i in range(len(some_list)):
		new_list.append(some_list[i]/2)
	return new_list

# Write a function that takes a list of words and returns a
# list of all the lengths of those words.
def word_lenths(word_list):
	new_list = [] 

	for i in range(len(word_list)):
		new_list.append(len(word_list[i]))

	return new_list

# Write a function (using iteration) that sums all the 
# numbers in a list.
def sum_numbers(numbers):
	if len(numbers) == 0:
		return None

	total = 0
	for i in range(len(numbers)):
		total += numbers[i]

	return total

# Write a function that multiplies all the numbers in a list together.
def mult_numbers(numbers):
	if len(numbers) == 0:
		return None

	total = 1
	
	for i in range(len(numbers)):
		total *= numbers[i]

	return total

# Write a function that joins all the strings in a list together 
# (without using the join method) and returns a single string.
def join_strings(string_list):
	new_string = ""

	for i in range(len(string_list)):
		new_string += string_list[i]

	return new_string

# Write a function that takes a list of integers and returns the
# average (without using the avg method)
def average(numbers):
	if len(numbers) == 0:
		return None

	sum_of_numbers = 0

	for i in range(len(numbers)):
		sum_of_numbers += numbers[i]

	if sum_of_numbers == 0:
		return 0

	return sum_of_numbers/len(numbers)


####################################################################

some_list = range(20)
# print some_list

words = ["girl", "boy", "person", "dog"]
# print words

int_list = [342,6,3,23,2,8,21,89,378]
print int_list

# tests
# print all_odd(some_list)
# print all_even(some_list)
# print long_words(words)
# print smallest(int_list)
# print largest(int_list)
# print halvesies(int_list)
# print word_lenths(words)
# print sum_numbers(int_list)
# print mult_numbers(int_list)
# print join_strings(words)
print average(int_list)
