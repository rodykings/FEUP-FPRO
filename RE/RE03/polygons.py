import turtle

window = turtle.Screen()
polygon = turtle.Turtle()
polygon.hideturtle()
polygon.pensize(5)

for n in [3,4,6,8]:
    for i in range(1, n+1, 1):  
        polygon.forward(100)
        polygon.left(360/ n)

