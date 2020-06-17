def fadd(n, m):
    s = n + m
    print(n,"+",m,'=',s)

while True:
    a = int(input("첫 번쨰 정수 입력 :"))
    b = int(input("두 번쨰 정수 입력 :"))

    if a==0 :        
        break
        
    else:
        fadd(a, b)

#a값과 b값이 동시에 0
