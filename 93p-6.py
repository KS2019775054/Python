x1 = int(input("x1 :"))
x2 = int(input("x2 :"))
y1 = int(input("y1 :"))
y2 = int(input("y2 :"))
c = ((x1-x2)**2 + (y1-y2)**2)**0.5

print(c)
import turtle
t = turtle.Turtle()
t.goto(x1,y1)
t.goto(x2,y2)

t.write("길이 " + str(((x1-x2)**2 + (y1-y2)**2)**0.5))
t.write("길이",c)
