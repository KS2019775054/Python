import random

a  = random.randint(1,100)
d  = random.randint(1,100)
b = a-d

print(a,"-",d , " ",  end =':::' )
c = int(input("="))
if c == b :
    print("정답")
else :
    print("오답")
