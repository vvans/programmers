def solution(triangle):
    max_r=[triangle[0]]
    for i in range(1,len(triangle)):
        l=[]
        for j in range(len(triangle[i])):
            l.append(0)
        l[0]=max_r[i-1][0]+triangle[i][0]
        l[len(triangle[i])-1]=max_r[i-1][len(triangle[i])-2]+triangle[i][len(triangle[i])-1]
        max_r.append(l)
    for i in range(2,len(triangle)):
        for j in range(1,len(triangle[i])-1):
            m=max(max_r[i-1][j-1],max_r[i-1][j])
            max_r[i][j]=m+triangle[i][j]
    

        
    return max(max_r[len(max_r)-1])
a=[[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]	
print(solution(a))