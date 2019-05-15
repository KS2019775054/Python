import turtle
t = turtle.Turtle()
import random
for i in range(50):
    number = random.randint(1,100)
    angle = random.randint(1,360)
    t.forward(number)
    t.left(angle)
