def solution(progresses, speeds):
    index=0
    l=len(progresses)
    progresses.append(0)
    answer = []
    while l>index:
        if progresses[index]>=100:
            x=1
            while True:
               index+=1
               if progresses[index]<100:
                 break 
               x+=1 
                
                
            answer.append(x)
        for i in range(l):
            progresses[i]+=speeds[i]
        
    return answer

a=[93, 30, 55]	
b=[1, 30, 5]	
print(solution(a,b))