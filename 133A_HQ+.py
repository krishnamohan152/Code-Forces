#! /usr/bin/env python

# Headers
import sys

# Input
Get_Input = input()

# Main Code
def main(Get_Input):
	Get_Str_In = Get_Input
	if "H" in Get_Str_In or "Q" in Get_Str_In or "9" in Get_Str_In:
		print("YES")
	else:
		print("NO")

if __name__ == '__main__':
	main(Get_Input)