import turtle as t
import random


t.speed(0)
t.penup()

t.pendown()

for i in range(1000):
    for j in range(4):
        
        t.forward(200)
        t.left(90)
    a = random.randint(-100,100)
    b = random.randint(-100,100)
    t.penup()
    t.goto(a,b)
    t.pendown()
        
