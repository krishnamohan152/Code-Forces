#! /usr/bin/env python

# Headers
import sys

# Main Code
def main(Get_Input):
	Count_A = 0
	Count_D = 0
	for i in Get_Input:
		if "A" in i:
			Count_A +=1
		else:
			Count_D +=1
	if Count_A > Count_D:
		p = ("Anton")
	elif Count_D > Count_A:
		p = ("Danik")
	else:
		p = ("Friendship")
	print(p)

# Input
Get_Input_Len = int(input())
Get_Input = input()
if Get_Input_Len == len(Get_Input):
	main(Get_Input)
else:
	pass