'''
Define a function solver(a, b, c) that returns the solution to the quadratic 
formula of the type: ax²+bx+c=0. Return the result in the form of a list: empty
list if no solution exists in ℝ, a list with one or two elements if one or two
solutions exist, respectively; if there are two solutions, use ascending order.
'''

def solver(a, b, c):

	verify = (b**2)-(4*a*c)

	if verify > 0:
		result = sorted(((-b+(verify)**(1/2))/(2*a), (-b-(verify)**(1/2))/(2*a)))
	elif verify == 0:
		result = [-b/(2*a)]
	else:
		result = []