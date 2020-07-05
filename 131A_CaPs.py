#! /usr/bin/env python

# Headers
import sys

# Input
Get_Input = input()

# Main Code
def main(Get_Input):
   
	if Get_Input.isupper():
		print(Get_Input.lower())
	elif str.upper(Get_Input[1:]) == Get_Input[1:]:
		print((Get_Input[0].upper())+(Get_Input[1:].lower()))
	else:
		print(Get_Input)

# Main fn
if __name__ == '__main__':
	main(Get_Input)