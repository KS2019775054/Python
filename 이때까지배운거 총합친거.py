asum = 0

def one(a):
    asum = 0
    for i in range(1,a+1):
        asum += i
    print("----------------------------")
    print("****************************")
    print(a,"까지의 정수의 합은 ",asum,"입니다")

def two(a,b,c):
    g = 0
    for i in range(a,b+1):
        if i%c == 0:
            g = g + i
    print("----------------------------")
    print("****************************")            
    print("%d에서 %d까지 %d의 배수의 합은 %d입니다." %(a,b,c,g))

def three(a):
    print("----------------------------")
    print("****************************")

    for i in range (1,10):
        print(a,"*",str(i)," = ", a*i)


   

while True:
    print("****************************")
    print("----------------------------")
    print(" 1. n까지의 정수의합  ")
    print(" 2. n~m까지 K의 배수의합  ")
    print(" 3. 구구단출력  ")
    print(" 4. 종료  ")
    menu = input("메뉴번호를 입력하세요 : ")


    if menu =="1":
        a = int(input("정수 입력 : "))
        one(a)
    if menu =="2":
        a = int(input("시작값 입력 : "))
        b = int(input("끝 값 입력 : "))
        c = int(input("배수를 입력하세요 : "))
        two(a,b,c)
    if menu =="3":
         a = int(input("정수 입력 : "))
         three(a)
    if menu == "4":
        break
            
        
                    
