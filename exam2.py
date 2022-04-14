import turtle
wn = turtle.Screen()
stars = turtle.Turtle()
wn.bgcolor("lightgreen")
stars.color("black")
stars.pensize(2)
stars.speed(10)
for i in range(5):
    for a in range(5):
        stars.pendown()
        stars.forward(100)
        stars.right(144)
    stars.penup()
    stars.forward(350)
    stars.right(144)