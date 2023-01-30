def solution(brown, yellow):
    answer = []
    a=int((b-4)/2)
    for i in range(a-1,0,-1):
        if i*(a-i)==yellow:
            answer=[max(i+2,a-i+2),min(i+2,a-i+2)]
    return answer

a=24
b=24
print(solution(a,b))