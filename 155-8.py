import turtle
t = turtle.Turtle()


bx1 = int(input("큰원의 중심 x : "))
by1 = int(input("큰원의 중심 y : "))
br = int(input("큰원 반지름 :"))
x1 = int(input("작은원 중심 x : "))
y1 = int(input("작은원 중심 y : "))
r = int(input("작은원 반지름 : "))

t.penup()
t.goto(bx1,by1)
t.pendown()
t.circle(br)

t.penup()
t.goto(x1,y1)
t.pendown()
t.circle(r)

l = ((bx1-x1)**2+(by1-y1)**2)**0.5

if br >=l+r  and br>=r:
    t.write("두번째 원이 첫번째 원의 내부에 있습니다.")

else:
            t.write("두번째 원이 첫번째 원의 내부에 없습니다.")
