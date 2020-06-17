s = 0

for i in range(1,101):
    s = s+i         #s += i

print("1부터 100까지의 합 =", s)
    
s = 0

for i in range(1,101,2):
    s = s+i         #s += i

print("1부터 100까지의 홀수들의 합 =", s)
    
s = 0

for i in range(2,101,2):
    s = s+i         #s += i

print("1부터 100까지의 짝수들의 합 =", s)

s = 0

for i in range(1,101):
    if i%2 == 0:
        s = s+i         #s += i

print("1부터 100까지의 짝수들의 합 =", s)

s = 0

for i in range(1,101):
    if i%2 == 1:
        s = s+i         #s += i

print("1부터 100까지의 짝수들의 합 =", s)


even_sum = 0
odd_sum = 0
for i in range(101):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i
print('1부터 100까지의 홀수들의 합 =',odd_sum)
print('1부터 100까지의 짝수들의 합 =',even_sum)

    
s = 0

for i in range(101):
    if i % 7 == 0:
        s = s+i         #s += i

print("1부터 100까지의 짝수들의 합 =", s)
