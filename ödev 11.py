import turtle;
wn = turtle.Screen()
yıldız = turtle.Turtle()
yıldız.speed(5)
yıldız.pensize(3)
i = 1
while(i <=5 ):
    yıldız.forward(100)
    yıldız.right(144)
    i += 1
    yıldız.hideturtle()
turtle.done()