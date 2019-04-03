a = int(input("몇각형을 그릴까요?"))


import turtle
t = turtle.Turtle()

for i in range(a) :
    t.forward(100)
    t.left(360/a)
