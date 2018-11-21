
def inner(u, v):
    result = 0

    for i in range (0, len(u)):
            result += u[i] * v[i]
    return result

print(inner([1,2,3,4,5],[2,3,4,5,6]))
