import turtle

window = turtle.Screen()
window.bgcolor("green")

alex = turtle.Turtle()
alex.color("blue")
alex.pensize(3)
alex.shape("turtle")
alex.stamp()

angle = 30

for i in range(0, 12, 1): 
    alex.penup()
    alex.left(angle)
    alex.forward(100)
    alex.pendown()
    alex.forward(10)
    alex.penup()
    alex.forward(20)
    alex.stamp()
    alex.backward(130)
