# lesson 10 sqaure peoject
import turtle

screen = turtle.Screen()
screen.bgcolor("black")  
screen.title("Turtle Square Drawing")

pen = turtle.Turtle()
pen.color("white")
pen.pensize(8)
pen.speed(2)

for _ in range(4):
    pen.forward(100)
    pen.left(90)     

pen.hideturtle()
turtle.done()