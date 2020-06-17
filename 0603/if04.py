# file name : if04py

num = int(input('하나의 수를 입력하시오'))

result = '3의 배수도 아니고 5의 배수도 아닙니다.'

if num%3 == 0:
    result = '3의 배수입니다'
if num%5 == 0:
    result = '5의 배수입니다'
if num%3 == 0 and num%5 == 0:
    result = '3의 배수이고 5의 배수입니다.'

print(result)
