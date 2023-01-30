def solution(rectangle, characterX, characterY, itemX, itemY):
    def make_map(x1,y1,x2,y2):
        for i in range(y1,y2+1):
            maps[x1][i]=1
        for i in range(y1,y2+1):
            maps[x2][i]=1
        for i in range(x1,x2+1):
            maps[i][y1]=1
        for i in range(x1,x2+1):
            maps[i][y2]=1
        return 0
    def make_line(l):
        for i in range(l):
            for j in range(l):
                if maps[i][j]!=1:
                    maps[i][j]=2
                else:
                    break
        for i in range(l):
            for j in range(l):
                if maps[j][i]!=1:
                    maps[j][i]=2
                else:
                    break
        for i in range(l-1,-1,-1):
            for j in range(l-1,-1,-1):
                if maps[i][j]!=1:
                    maps[i][j]=2
                else:
                    break
        for i in range(l-1,-1,-1):
            for j in range(l-1,-1,-1):
                if maps[j][i]!=1:
                    maps[j][i]=2
                else:
                    break
    for i in range(len(rectangle)):
        for j in range(4):
            rectangle[i][j]*=2
    max_x = max(map(max, rectangle))
    max_x+=2
    maps=[[0]*max_x for i in range(max_x)]
    for i in rectangle:
        x1=i[0];y1=i[1];x2=i[2];y2=i[3]
        make_map(x1,y1,x2,y2)
    make_line(max_x)
    def way2(x,y):
        a=max(maps[x-1][y-1],maps[x-1][y],maps[x-1][y+1],
        maps[x][y-1],maps[x][y+1],maps[x+1][y-1],maps[x+1][y],maps[x+1][y+1])
        if a==2:
            return True
    def way(x,y):
        if visit[x+1][y]==1 and way2(x+1,y):
            return x+1,y
        elif visit[x-1][y]==1 and way2(x-1,y):
            return x-1,y
        elif visit[x][y+1]==1 and way2(x,y+1):
            return x,y+1
        elif visit[x][y-1]==1 and way2(x,y-1):
            return x,y-1
        else:
            print(x,y)
            return 1,1
    x=characterX*2
    y=characterY*2
    visit=maps
    cnt=0
    answer=[]
    while True:
        visit[x][y]=0
        x,y=way(x,y)
        cnt+=1
        if x==1 and y==1:
            answer.append(cnt/2)
            break
        if x==itemX*2 and y==itemY*2:
            answer.append(cnt/2)
            cnt=0

    return int(min(answer))

a=[[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]]	
b=1
c=2
d=1
e=3
print(solution(a,b,c,d,e))