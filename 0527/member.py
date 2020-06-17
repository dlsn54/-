#멤버 연산은 그룹내에(list, tuple, dictionary, set) 내에 존재유무
#결과는 논리값

list_a = [3, 4, 5, 6, 7, 8]
a = int(input('찾고자 하는 element : '))

print('list_a에', a ,'가 있습니다.',(a in list_a))
print('list_a에', a ,'가 없습니다.',(a not in list_a))




