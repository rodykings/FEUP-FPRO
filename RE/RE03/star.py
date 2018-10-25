
import turtle

window = turtle.Screen()
window.bgcolor("blue")

alex = turtle.Turtle()
alex.color("white")
alex.shapesize(0.75)
alex.shape("circle")
alex.pensize(1.5)
alex.stamp()

angle = 45

for i in range(0, 8, 1): 
    alex.left(angle)
    alex.forward(100)
    alex.stamp()
    alex.backward(100)
