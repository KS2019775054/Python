import turtle as t


t.speed(1)
for i in range(1000):

    t.penup()
    t.speed(0)
    t.goto(-300,0)
    t.pendown()
    t.hideturtle();

    if i%8 ==1:
        t.write(" @(^0^)@ ",font =("Arial",90,"normal"))
    elif i%8 ==2:
        t.write(" @=(^0^)@ ",font =("Arial",90,"normal"))
    elif i%8==3:
        t.write(" @==(^0^)@ ",font =("Arial",90,"normal"))
    elif i%8==4:
        t.write(" @=(^0^)@ ",font =("Arial",90,"normal"))
    elif i%8==5:
        t.write(" @(^0^)@ ",font =("Arial",90,"normal"))
    elif i%8==6:
        t.write(" @(^0^)=@ ",font =("Arial",90,"normal"))
    elif i%8==7:
        t.write(" @(^0^)==@ ",font =("Arial",90,"normal"))
    elif i%8==0:
        t.write(" @(^0^)=@ ",font =("Arial",90,"normal"))
    t.hideturtle();
    t.color("white")
    t.speed(0)
    t.penup()
    t.forward(80)  
    t.reset()

        
        
    
