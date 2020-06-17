def calc_gugudan(dan):
    for i in range(1, 10):
        print(dan,"*",i,"=",(dan*i))

while True:
    d= int(input("단 입력 :"))
    if d >= 1 and d <= 9: # 1 <= d <=9
        calc_gugudan(d)
    else:
        print("1부터 9사이의 단을 출력합니다")
        break
