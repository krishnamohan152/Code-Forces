#! /usr/bin/env python

# Headers
import sys

# Input
Get_Char = input()

# Main Code
def main(Get_Char):
	Get_Char_Lower = Get_Char.lower()
	Get_Vowels = Get_Char_Lower.replace('a','').replace('o','').replace('y','').replace('e','').replace('u','').replace('i','')
	Insert_Char = '.'.join(Get_Vowels)
	Fin_result = '.'+Insert_Char
	print(Fin_result)

if __name__ == '__main__':
	main(Get_Char)