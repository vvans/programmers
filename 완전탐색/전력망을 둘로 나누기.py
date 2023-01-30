def solution(n, wires):
    def DFS(s,dfs,n):
        for i in range(1,n+1):
            if dfs[s][i]==1 and visit[i]==0:
                visit[i]=1
                DFS(i,dfs,n)
    dfs=[[0]*(n+1)for i in range(n+1)]
    for i in range(len(wires)):
        s=wires[i][0]
        e=wires[i][1]
        dfs[s][e]=1
        dfs[e][s]+=1
    min=n
    for i in range(len(wires)):
        s=wires[i][0]
        e=wires[i][1]

        visit=[0 for i in range(n+1)]
        visit[s]=1
        visit[e]=1
        DFS(s,dfs,n)
        num1=visit.count(1)-1
        visit=[0 for i in range(n+1)]
        visit[s]=1
        visit[e]=1
        DFS(e,dfs,n)
        num2=visit.count(1)-1
        if min>abs(num1-num2):
            min=abs(num1-num2)
    return min
a=[[1,2],[2,3],[3,4]]	
print(solution(4,a))