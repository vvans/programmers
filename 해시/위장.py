from itertools import combinations

def solution(clothes):
    li=[i[1] for i in clothes]
    li.sort()
    fi=li[0]
    num=[]
    for i in range(len(li)):
        if li[i]!=fi:
            num.append(li.count(fi)+1)
            fi=li[i]
    num.append(li.count(fi)+1)
    ans=1
    for i in num:
        ans*=i

    return ans-1

        
a=[["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(a))