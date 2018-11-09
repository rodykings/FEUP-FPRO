import statistics
import random
import math

#SQUARE 2x2
square_lenght = 2
square_area = square_lenght**2

#CIRCLE 
r_circle = 1

#NEEDLES IN CIRCLE
def needles_in(amount):
    needles_circle = 0
    for i in range (0, amount, 1):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if math.sqrt((x**2) + (y**2)) < r_circle:
            needles_circle += 1
    return needles_circle

#MONTE CARLO FORMULA
def monte_carlo(needles_square):
    return (square_area * needles_in(needles_square)) / needles_square

def main():
    print(monte_carlo())

if __name__ == "__main__":
    main()
