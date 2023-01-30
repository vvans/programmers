def solution(wor):
    word=[]
    for i in range(len(wor)):
        word.append(wor[i])
    for i in range(5-len(wor)):
        word.append('')
    w=['A','E','I','O','U']
    cnt=0
    for i in w:
        word_list=['']*5
        word_list[0]=i
        cnt+=1
        if word_list==word:
            return cnt
        for j in w:
            word_list[1]=j
            cnt+=1
            if word_list==word:
                return cnt
            for l in w:
                word_list[2]=l
                cnt+=1
                if word_list==word:
                    return cnt
                for k in w:
                    word_list[3]=k
                    cnt+=1
                    if word_list==word:
                        return cnt
                    for h in w:
                        word_list[4]=h
                        cnt+=1
                        if word_list==word:
                            return cnt
                    word_list[4]=''
                word_list[3]=''
            word_list[2]=''
        word_list[1]=''

    return 0
a="AAAAE"
solution(a)