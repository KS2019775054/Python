import turtle
t = turtle.Turtle()

n = int(turtle.textinput("","몇각형?"))

for i in range(n):
    t.forward(100)
    t.left(360/n)
