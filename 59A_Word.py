#! /usr/bin/env python

# Header
import sys

# Input 
Get_input = input()

# Main Code
def main(Get_input):
	Chr_upper,Chr_lower=0,0
	for i in Get_input:
		if i.isupper():
			Chr_upper+=1
		elif i.islower():
			Chr_lower+=1

	if Chr_lower == Chr_upper:
		print(Get_input.lower())
	elif Chr_lower > Chr_upper:
		print(Get_input.lower())
	else:
		print(Get_input.upper())

if __name__=='__main__':
	main(Get_input)