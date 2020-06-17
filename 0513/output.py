#  출력에 대하여 알아보자
print("하나","둘","셋",1,2,3) 
print("하나","둘","셋",1,2,3,sep='-') 
print("첫번째 값")
print("두번째 값") # 다른 줄에 출력
print("첫번째 값", end=" ---> ")
print("두번째 값") # 같은 줄에 출력
print("첫번째 값", end=" ")
print("두번째 값") # 같은 줄에 출력
print("첫번째 값", end="")
print("두번째 값") # 같은 줄에 출력
print('Hello World!!')
print("Hello World!!") #syntax
print("나의 이름은 '한사람'입니다.")
print('나의 이름은 "한사람"입니다.')
print("나의 이름은 \"한사람\"입니다.")
print('나의 이름은 \'한사람\'입니다.')
print('-' * 40)
print('   {} {}   '.format(1,2))
print('   {0} {1}   '.format(1,2))
print('   {1} {0}   '.format(1,2))
print('   {0} {1} {2}  '.format(1,2,3))
print('   {2} {1} {0}  '.format(1,2,3))
print('   *{2:10}*  *{1:10}*  *{0:10}*  '.format(1,2,3))
print('-' * 40)
print('Python is [{:15}]'.format('good'))
print('Python is [{:<15}]'.format('good'))
print('Python is [{:>15}]'.format('good'))
print('Python is [{:^15}]'.format('good'))
print('당신의 나이는 [{:15}]세'.format(22))
print('당신의 나이는 [{:<15}]세'.format(22))
print('당신의 나이는 [{:>15}]세'.format(22))
print('당신의 나이는 [{:^15}]세'.format(22))
print('-' * 40)
print("I eat %d apples." % 3)
print("I eat %d apples. & %d bananas." % (3,1))
print('-' * 40)

