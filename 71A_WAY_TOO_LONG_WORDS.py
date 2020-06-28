#! /usr/bin/env python

# Headers
import sys

# Input
Get_Num = int(input())

for i in range(1,Get_Num+1):
	Get_Char = input()
# Main Body
	if len(Get_Char) > 10:
		Start_Char = Get_Char[0]
		Last_Char = Get_Char[-1:]
		Rest_Char = Get_Char[1:-1]
		Total = Start_Char+str(len(Rest_Char))+Last_Char
		print(Total)
	else:
		print(Get_Char)