
def evaluate(a, x):
    return sum([v*x**i for i,v in enumerate(a)])

print(evaluate([1, 2, 4, 6, 8], 2))