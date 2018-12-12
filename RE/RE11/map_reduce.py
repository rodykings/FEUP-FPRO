#2.map_reduce
from functools import reduce

def map_reduce(n1, n2):
    return reduce((lambda x, y: x * y if x*y<50 else x+y), [i**2 for i in range(n1, n2, 1) if i%2==1])
