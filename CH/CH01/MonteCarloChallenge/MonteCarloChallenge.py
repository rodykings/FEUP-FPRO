import random
import math

#SQUARE 2x2
square_lenght = 2
square_area = square_lenght**2

#CIRCLE 
r_circle = 1

#THROWING NEEDLES
def throw_needles(amount):
    needles_position = []
    for i in range(0, amount*2):
        needles_position.append(random.uniform(-1, 1))
    return needles_position

#NEEDLES IN CIRCLE
def needles_in(amount):
    needles_circle = 0
    for i in range (0, amount*2, 2):
        if (math.sqrt(((throw_needles(amount)[i])**2) + ((throw_needles(amount)[i+1])**2))) > r_circle:
            continue
        else:
            needles_circle += 1
    return needles_circle

#MONTE CARLO FORMULA
def monte_carlo(needles_square):
    return (square_area * needles_in(needles_square)) / needles_square

def main():
    print(monte_carlo(2000))

if __name__ == "__main__":
    main()
