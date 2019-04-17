import turtle
t = turtle.Turtle()

s = turtle.textinput("","도형을 입력하시오 :")

if s == "사각형":
    a = int(turtle.textinput("","가로"))
    b = int(turtle.textinput("","세로"))
    t.forward(a)
    t.left(90)
    t.forward(b)
    t.left(90)
    t.forward(a)
    t.left(90)
    t.forward(b)

elif s == "삼각형":
    a = int(turtle.textinput("","크기"))
    t.forward(a)
    t.left(120)
    t.forward(a)
    t.left(120)
    t.forward(a)
    t.left(120)
elif s == "원":
     a = int(turtle.textinput("","크기"))
     t.circle(a)
else:
    t.write("삼각형,사각형,원 중에 고르시오 ")
