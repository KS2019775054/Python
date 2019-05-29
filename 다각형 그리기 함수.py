a = int(input("몇각형을 그릴까요? "))

import turtle as t
t.speed(0)

def ff (a):
    for j in range (3000):
        for i in range(a) :
            t.forward(100)
            t.left(360/a)
        t.left(29)
    
ff(a)
