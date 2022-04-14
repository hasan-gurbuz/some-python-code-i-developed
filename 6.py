def draw_equitriangle(t,sz):
    for i in range (sz):
        t.forward(80)
        t.left(120)
import turtle
wn = turtle.Screen()
wn.bgcolor("green")
hasan = turtle.Turtle()
hasan.color("red")
draw_equitriangle(hasan,3)
turtle.done()