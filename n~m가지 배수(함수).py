a = int(input("시작값 입력 : "))
b = int(input("끝 값 입력 : "))
c = int(input("배수를 입력하세요 : "))


def ffff(a, b, c):
    d = 0
    for i in range(a,b+1):
        if i%c == 0:
            d = d+i
    return d

print(ffff(a,b,c))
