
def comp(seq):                                                #상보적 변환 함수      
    comp_dict = {"A":"T","T":"A","C":"G","G":"C"}             #DNA 변환문자
    seq_comp = ""                                             #seq_comp 미리 공백 처리
    for char in seq:                                          #for문으로 seq값을 char에 넣음
        if char in comp_dict:                                 #if문으로 comp_dict에 char가 있는 것만 실행
            seq_comp += comp_dict[char]                       #seq_comp에 if 문 값을 추가
        else:                                                 #if가 아니라면
            seq_comp += "?"                                   #if가 아닌것은 ? 로 처리
    return seq_comp                                           #seq_comp 값을 리턴

def rev(seq):                                                 #역순 변환 함수
    seq_dna ="ATGC"                                           #DNA값 표준을 설정
    seq_rev=""                                                #seq_rev 공백 처리
    for char in seq:                                          #for문으로 seq값을 char에 넣음
        if char in seq_dna:                                   #seq_dna값이 char에 들어있지 있다면
            seq_rev += char                                   #seq_rev값에 if문이 맞다면 추가
        else:                                                 #if가 아니라면
            seq_rev += "?"                                    #아니라면 ?값으로 처리
    seq_rev = "".join(reversed(seq_rev))                      #seq_rev값을 거꾸로 바꿈
    return seq_rev                                            #seq_rev값을 리턴함
    
def rev_comp(seq):                                            #상보적 역순 변환 함수
    tmp = comp(seq)                                           #tmp에 comp함수값을 넣음
    return rev(tmp)                                           #rev(tmp)값을 리턴함

src = input("DNA")                                            #src입력

cnvt = int(input("상보적1 역순2 상보적 역순3"))               #cnvt입력

if (cnvt >= 1 and cnvt <= 3):                                 #cnvt 혹시 cnvt값이 1보다크거나 같고 3보다 작거나 같으면
    if (cnvt == 1):                                           #cnvt가 1이면 
        rst = comp(src)                                       #comp함수를 src값을 넣어서 실행해서 rst에 넣는다
    elif (cnvt == 2):                                         #cnvt가 2면 
        rst = rev(src)                                        #rev함수를 src값을 넣어서 실행해서 rst에 넣는다
    else:
        rst = rev_comp(src)
    print(src, "->", rst)
else:
    print("1(comp),2(Rev), 3(Rev_Comp)!!")

    
