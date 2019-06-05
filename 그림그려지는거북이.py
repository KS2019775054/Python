import turtle as t

def square(length):
    for i in range(4):
        t.forward(length)
        t.left(90)


def drawit(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    t.color("green")
    square(50)
    t.end_fill()

s = t.Screen() #그림이 그려지는 화면얻는다
s.onscreenclick(drawit)
