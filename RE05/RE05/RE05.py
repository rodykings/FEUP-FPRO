
def mastermind(g1, g2, g3, c1, c2, c3):
    points = 0
    
    #right guess
    if g1 == c1:
        points += 3
        if g2 == c2:
            points += 3
            if g3 == c3:
                points += 3
                return points

    