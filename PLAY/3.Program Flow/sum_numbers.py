#Define a function f(n) that returns the sum of numbers 1+2+...+n.

def f(n):
	sum = 0
	while n > 0:
		sum += n
		n= n-1
	return sum