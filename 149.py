import random

a = input("어디를 수비하시겠어요? (왼쪽,중앙,오른쪽,) : ")


b = ["왼쪽","중앙","오른쪽"]

c = random.choice(b)



if c ==a:
    print("수비성공")
else:
    print("수비실패")
