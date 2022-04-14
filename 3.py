def draw_poly(t,n,sz):
    for i in range(n):
        t.forward(sz)
        t.left(45)
import turtle
wn = turtle.Screen()
wn.bgcolor("green")
tess = turtle.Turtle()
tess.color("red")
tess.pensize(2)
tess.speed(4)
draw_poly(tess,8,50)
turtle.done()