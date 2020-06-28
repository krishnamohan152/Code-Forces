#! /usr/bin/env python

# Headers
import sys

# Input
Get_Num = input()

# Main Code
def main(Get_Num):
	if int(Get_Num) == 2:
		print("NO")
	elif int(Get_Num) % 2 == 0:
		print("YES")
	else:
		print("NO")


if __name__ == '__main__':
	main(Get_Num)