
from math import *


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


def pDiv(n):
	if(prime(n)):
		return [[n], [1]]
	else:
		pDiv = []
		nDiv = []
		if(n%2 == 0):
			pDiv.append(2)
			q = 1; n = n/2
			while(n%2 == 0):
				q += 1
				n = n/2
			nDiv.append(q)
		cuenta = 3
		while(n != 1 ):
			if(n%cuenta == 0) :
				pDiv.append(cuenta)
				q = 1; n = n/cuenta
				while(n%cuenta == 0):
					q += 1
					n = n/cuenta
				nDiv.append(q)
			cuenta += 2
		return [pDiv, nDiv]


def triang(n):
	return n * (n+1) / 2

def nDiv( heh):
	a = 0
	total=1
	while(a < len(heh)):
		total = (heh[a] +1)*total
		a += 1
	return total



def eu12():
	q = 3
	div = 1
	while(div < 500):
		q = q+1
		a = triang(q)
		rta = pDiv(a)
		div = nDiv(rta[1])
		print("vamos en la posicion %d, el numero %d, con %d divisores" %(q, a, div))
	print("la respuesta es el %d, con %d divisores" %(a,div))

def dir(n):
	return nDiv(pDiv(n)[1])



print dir(20)
print dir(28)
eu12()









	
