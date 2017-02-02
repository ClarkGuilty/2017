
import math


def prime(a):
	if (a == 2):
		return True
	if ( a%2 == 0):
		return False
	if(a == 1):
		return False
	b = 3.0
	while(b<= sqrt(a)):
		if(a%b == 0):
			return False
		b +=2
	return True

def fib(n):
	a, b = 0, 1
	for i in range(0, n):
		a, b = b, a + b
	return a


def nDigitsFib(n):
	i = 0
	j = 0
	while(n>i):
		j = j + 1
		k = fib(j)
		h = math.log10(k)
		h = math.floor(h)
		i = h + 1
		print("Voy en el elemento %d con  %d digitos." % (j,i))



	
