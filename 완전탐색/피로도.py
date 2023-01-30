from itertools import permutations
def solution(k, dungeons):
    x=[]
    answer = -1
    for i in range(1,len(dungeons)+1):
        a=list(permutations(dungeons, i))
        for i in range(len(a)):
            x.append(a[i])
    for i in x:
        k1=k
        cnt=0
        l=0
        for j in i:
            if k1>=j[0]:
                k1-=j[1]
                cnt+=1
            else:
                break
        if answer<cnt:
            answer=cnt

            

    return answer

a=80
b=[[80,20],[50,40],[30,10]]	
print(solution(a,b))