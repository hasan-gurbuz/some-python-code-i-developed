import turtle;
wn =turtle.Screen()
wn.bgcolor("green")
hasan = turtle.Turtle()
hasan.pencolor("red")
hasan.pensize(2)
for i in range(5):
    for a in range(4):
        hasan.forward(20)
        hasan.left(90)
    hasan.forward(20)
    hasan.penup()
    hasan.forward(20)
    hasan.pendown()
turtle.done()
