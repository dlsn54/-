def print19(start,end):
    for i in range(start,end+1):
        print(i,end=" ")
    print("")
while True:
    s = int(input('시작 값 :'))
    e = int(input("끝 값 :"))

    if s < e :
        print19(s,e)
    else:
        print("시작 값이 끝 값보다 큽니다.")
        break
