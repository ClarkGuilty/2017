from math import *

def prime(a):
	if(a == 2):
		return True
	if(a%2 == 0):
		return False
	if(a == 1):
		return False
	b = 3.0
	while(b <= sqrt(a)):
		if(a%b == 0):
			return False
		b +=2
	return True
