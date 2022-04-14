def olayYeri(trt,git):
    trt.pendown()
    for x in range(4):
        trt.forward(git)
        trt.left(90)
    trt.penup()
    trt.backward(10)
    trt.right(90)
    trt.forward(10)
    trt.left(90)
import turtle
wn = turtle.Screen()
wn.bgcolor("green")
hasan=turtle.Turtle()
hasan.color("red")
hasan.pensize(2)
hasan.speed(5)
for i in range(5):
    olayYeri(hasan,20+20*i)
turtle.done()