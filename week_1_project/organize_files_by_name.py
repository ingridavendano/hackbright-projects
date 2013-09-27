# Created by Ingrid Avendano on 9/27/13.
# 
# 
# Week 1 Exercise
# 
# 1. Create 26 directories in the current directory, one for each letter of the
#	 alphabet:
# 		./a/
# 		./b/
# 		./c/
#  		etc.
# 
# 2. Loop through all the files in the original_files directory, and organize 
#	 each of those files into the directory that their name starts with.


import os
import shutil


def main():
	alphabet = list("abcdefghijklmnopqrstuvwxyz")
	directories = []

	# prompts the user to create a destination directory of lettered folders
	print "Provide a name for a directory:"
	dst_dir_name = raw_input("> ")
	dst_dir_path = "./" + dst_dir_name + "/"

	# create a destination directory to hold all the letters in
	os.mkdir(dst_dir_path)

	# creates a directory for every letter of the alphabet
	for letter in alphabet:
		new_dir_path = dst_dir_path + letter + "/"
		os.mkdir(new_dir_path)

	# files directory that is getting sorted
	src_dir_name = "./files/"
	list_of_txt_files = os.listdir(src_dir_name)

	# sorts every file into a letter directory and moves it
	for file_name in list_of_txt_files:
		letter = file_name[0]
		src_path = src_dir_name + file_name

		# new destination of txt file
		dst_path = dst_dir_path + letter + "/"
		shutil.move(src_path,dst_path)

main()
