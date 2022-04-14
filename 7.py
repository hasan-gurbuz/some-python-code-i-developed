from cgi import test
import turtle
def ucgen(hasan,sz):
    for i in range(3):
        hasan.forward(sz)
        hasan.left(120)
    hasan.penup()
    hasan.forward(50)
    hasan.pendown()
wn = turtle.Screen()
wn.bgcolor("lightgreen")
test = turtle.Turtle()
for i in range(5):
    ucgen(test,25)
wn.mainloop()