def solution(priorities, location):
    r=0
    l=len(priorities)
    answer = 0
    pri=0
    while True:
        if r+1==l:
            return pri+1
        if priorities[r]>=max(priorities[r+1:l]) and r==location:
            pri+=1
            return pri
        if priorities[r]>=max(priorities[r+1:l]):
            r+=1
            pri+=1
        else:
            priorities.append(priorities[r])
            r+=1
            l+=1
            if location<r:
                location=l-1
    


a=[2,1,5,3,9,9]	
b=1
print(solution(a,b))