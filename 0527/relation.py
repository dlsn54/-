#관계(비교)연산은 두 수의 대소 혹은 동등 관계를  연산해서
#Boolean(True, False) 값을 내어주는 연산


a = int(input('첫 번쨰 정수 : '))
b = int(input('두 번쨰 정수 : '))

print(a, '<', b, '=>', (a<b))
print(a, '<=', b, '=>', (a<=b))
print(a, '>', b, '=>', (a>b))
print(a, '>=', b, '=>', (a>=b))
print(a, '==', b, '=>', (a==b))
print(a, '!=', b, '=>', (a!=b))

