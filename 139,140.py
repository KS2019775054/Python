import turtle
t = turtle.Turtle()



while True:
    a = input("명령을 입력 : ")
    if a == "r":
        t.right(90)
        t.forward(100)
    if a == "l":
        t.left(90)
        t.forward(100)
        
    

