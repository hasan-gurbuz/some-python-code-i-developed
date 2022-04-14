shape = input("Please select a shape, triangle or square:")
lenght = int(input("please enter a lenght for your choose:"))
angle = int(input("please enter a angle for your choose:"))
import turtle
a=turtle.Screen()
meltem=turtle.Turtle()
if shape == "square":
    meltem.color("pink")
    meltem.shape("square")
    for i in range(4):
        meltem.forward(lenght)
        meltem.left(angle)
if shape =="triangle":
    meltem.color("pink")
    meltem.shape("triangle")
    for i in range(3):
        meltem.forward(lenght)
        meltem.left(angle)
turtle.done