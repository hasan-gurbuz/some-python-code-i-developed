import turtle
hasan = turtle.Turtle()
wn = turtle.Screen()
wn.bgcolor("green")
hasan.color("red")
hasan.speed(30)
hasan.pensize(2)
hasan.left(180)
n = 4
for i in range(94):
    hasan.forward(n)
    hasan.right(90)
    n += 4
turtle.done()