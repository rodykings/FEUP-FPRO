def mastermind(g1, g2, g3, c1, c2, c3):
    points = 0
    
    if g1 == c1:
        points += 3
    elif g1 == c2:
        points += 1
    elif g1 == c3:
        points += 1

    if g2 == c2:
        points += 3
    elif g2 == c1:
        points += 1
    elif g2 == c3:
        points += 1

    if g3 == c3:
        points += 3
    elif g3 == c2:
        points += 1
    elif g3 == c1:
        points += 1

    return points

print(mastermind("b", "w", "y", "b", "w", "y"))
print(mastermind("b", "b", "y", "b", "w", "b"))
print(mastermind("b", "w", "y", "w", "y", "w"))
        
