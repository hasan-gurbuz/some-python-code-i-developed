import turtle
wna = turtle.Screen()
wna.bgcolor("green")
hasan = turtle.Turtle()
hasan.speed(30)
hasan.color("blue")
hasan.pensize(2)
hasan.left(180)
n = 4
for i in range(84):
    hasan.forward(n)
    hasan.right(91)
    n += 4
turtle.done()