from itertools import permutations
def solution(numbers):
    answer = {}
    answer=set()
    for i in range(1,len(numbers)+1):
        a=list(permutations(numbers, i))
        for j in a:
            k=''
            for x in j:
                k+=x
            k=int(k)
            chk=True
            for l in range(2,k):
                if k%l==0:
                    chk=False
                    break
            if k>=2 and chk==True:
                answer.add(k)


    return len(answer)

a="011"
print(solution(a))