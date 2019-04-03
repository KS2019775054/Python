a = int(input("투입한 돈 :"))
b = int(input("물건값 :"))

print("거스름돈 =" ,a-b,)

print("500원 동전의 갯수 : ",(a-b)//500,)
print("100원 동전의 갯수 :" ,((a-b)%500)//100)
