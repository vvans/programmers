def solution(n, computers):
    chk=[0]*n
    def dfs(s,num):
        for i in range(n):
            if computers[s][i]==1 and chk[i]==0:
                chk[i]=num
                dfs(i,chk[i])

    for i in range(n):
        if chk[i]==0:
            chk[i]=max(chk)+1
            dfs(i,chk[i])


    return max(chk)

a=3
b=[[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(solution(a,b))