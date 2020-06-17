n = 0
s = 0
while n <= 100:
    n += 1
    if n % 7 == 0:
        continue
    s += n

print("1부터 100까지의 합 중에 7의 배수를 생략한 수들의 합은",s,"입니다")

