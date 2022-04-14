def draw_star():
    import turtle
    wn = turtle.Screen()
    wn.bgcolor("white")
    star = turtle.Turtle()
    star.color("black")
    for i in range (5):
        star.forward(100)
        star.right(144)
draw_star()