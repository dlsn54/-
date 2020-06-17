def fadd(n,m):
    s = n + m
    return s

def fsub(n,m):
    s = n - m
    return s

def favg(a, b ,c):
    avg = (a+b+c)/3
    return avg

a = int(input('첫 번째 정수 :'))

b = int(input('두 번째 정수 :'))

c = int(input('세 번째 정수 :'))

r = fadd(a,b)
print(a,"와",b,"의 합은",r,"입니다")

r = fsub(a,b)
print(a,"와",b,"의 차는",r,"입니다")

r = favg(a,b,c)
print("(",a,",",b,",",c,")의 평균은",r,"입니다")

