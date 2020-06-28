#! /usr/bin/env python

# Headers
m,n,a = input().split()
m,n,a = int(m),int(n),int(a)
# Main Code
def main(m,n,a):
	if m%a == 0:
		Cal_Square = int(m/a)
	else:
		Cal_Square = (int(m/a)+1)
	if n%a == 0:
		Cal_Square_1 = int(n/a)
	else:
		Cal_Square_1 = (int(n/a)+1)
	Total_Square_Reqd = Cal_Square_1*Cal_Square
	print(Total_Square_Reqd)

# Main fn
if __name__=="__main__":
	main(m,n,a)