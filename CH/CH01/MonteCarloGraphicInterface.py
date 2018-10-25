
import math
import random
import turtle
import statistics


#define square
square_lenght = 2000
square_area = square_lenght**2

#define circle
circle_r = square_lenght/2
circle_area = math.pi * (circle_r)**2

#define random points in the area of the square
point_x = []
point_y = []
in_points = 0
total_points = 1000

def turtleGraphics():
    #define turtle graphics
    window = turtle.Screen()
    window.setworldcoordinates(-1200, -1200, 1200, 1200)
    window.title("Monte Carlo Graphic Interface")
    window.delay(0)

    #draw square
    square = turtle.Turtle()
    square.hideturtle()
    square.shape()
    square.penup()
    square.right(90)
    square.forward(square_lenght/2)
    square.pendown()
    square.left(90)
    square.forward(square_lenght/2)
    square.left(90)
    square.forward(square_lenght)
    square.left(90)
    square.forward(square_lenght)
    square.left(90)
    square.forward(square_lenght)
    square.left(90)
    square.forward(square_lenght/2)

    #draw circle
    circle = turtle.Turtle()
    circle.hideturtle()
    circle.shape()
    circle.penup()
    circle.forward(square_lenght/2)
    circle.left(90)
    circle.pendown()
    circle.circle(circle_r)



#draw point 
point = turtle.Turtle()
def drawPoint(x_random, y_random):
     if verifyPoints(x_random, y_random) == 1:
         point.color("green")
     else:
         point.color("red")
         point.shape("circle")
         point.shapesize(0.1, 0.1)
         point.penup()
         point.setx(x_random)
         point.sety(y_random)
         point.pendown()
         point.stamp()

# draw points
def draw_points():
    for i in range(0, 1000, 1):
        drawPoint(point_x[i], point_y[i])

#draw text
def drawText(pi):
    text = turtle.Turtle()
    text.penup()
    text.setx(20)
    text.sety(-230)
    text.pendown()
    text.write("PI ~= " + str(pi) , move=False, align="left", font=("Arial", 10, "normal"))

#verify if points are in or out the circle
def verifyPoints(x_random, y_random):
    distance = math.sqrt(((x_random)**2 + (y_random)**2))
    if (distance > circle_r):
        return 0
    else:
        return 1

def monte_carlo_formula (square_area, in_points, total_points):
    return square_area * (in_points / total_points) 



turtleGraphics()

for i in range(0,total_points,1):
    x_random = random.uniform(-(square_lenght/2), square_lenght/2)
    y_random = random.uniform(-(square_lenght/2), square_lenght/2)
    point_x.append(x_random)
    point_y.append(y_random)
    in_points += verifyPoints(x_random, y_random)    
    
        
 
drawText(monte_carlo_formula(square_area, in_points, total_points))

