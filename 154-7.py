import random

a = random.randint(10,99)
print(a)
b = int(input("두자리 숫자 : "))

if a%10 == b%10 or a//10 ==b//10 :

    if a%10==b%10 and  a//10 ==b//10 :
        print("100만원 ㅊㅊ")
    else :
        print("50만원 ㅊㅊ ")
else:
    print("꽝")
