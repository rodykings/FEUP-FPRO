
import turtle

print("POLYGON TURTLE GRAPHIC" + "\n")
number_sides = int(input("Number of sides: "))
side_length = int(input("Side lenght: "))
border_color = input("Border color: ")
fill_color = input("Fill color: ")

internal_angle = 360 / int(number_sides)

window = turtle.Screen()
polygon = turtle.Turtle()
polygon.hideturtle()
polygon.pensize(5)
polygon.pencolor(border_color)
polygon.fillcolor(fill_color)
polygon.begin_fill()

for i in range(0, number_sides, 1):
    polygon.forward(side_length)
    polygon.left(internal_angle)
    
polygon.end_fill()