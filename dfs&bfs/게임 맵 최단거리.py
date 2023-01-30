def solution(maps):
    def way(x,y,w):
        w.append([x+1,y])
        w.append([x,y+1])
        w.append([x-1,y])
        w.append([x,y-1])
        
        return w
        
    def bfs(x,y,cnt,visit):
        visit[x][y]=1
        if x==len(maps)-1 and y==len(maps[0])-1:
            global min_v
            if  min_v==-1 or min_v>cnt:
                min_v=cnt
        w=[]
        way(x,y,w)
        r_w=[]
        for i in range(4):
            if not(min(w[i])==-1 or w[i][0]==n or w[i][1]==m):
                if maps[w[i][0]][w[i][1]]==1 and visit[w[i][0]][w[i][1]]==0:
                    r_w.append(w[i])
        for i in range(len(r_w)):
            bfs(r_w[i][0],r_w[i][1],cnt+1,visit)
            visit[r_w[i][0]][r_w[i][1]]=0
    
    global min_v
    min_v=-1
    cnt=0
    n=len(maps)
    m=len(maps[0])
    visit=[[0]*m for i in range(n)]
    bfs(0,0,1,visit)
    return min_v

a=[[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1],[0,0,0,0,1]]
print(len(a))
print(len(a[0]))
print(solution(a))