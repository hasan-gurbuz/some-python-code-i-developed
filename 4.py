def kare(isim,n):
    isim.pendown()
    isim.left(n)
    isim.forward(80)
    isim.left(90)
    isim.forward(80)
    for i in range(3):
        isim.left(90)
        isim.forward(160)
    isim.penup()
    isim.left(90)
    isim.forward(80)
    isim.right(90)
    isim.backward(80)
import turtle
wn = turtle.Screen()
wn.bgcolor("green")
hasan = turtle.Turtle()
hasan.color("red")
hasan.pensize(2)
hasan.speed(4)
for x in range(20):
    kare(hasan,18)
turtle.done