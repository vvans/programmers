def solution(arr):
    def cal(a,f,b):
        if f=='+':
            return int(a)+int(b)
        else:
            return int(a)-int(b)

    a=len(arr)//2+1
    maps=[[0]*a for i in range(a)]
    for i in range(len(arr)):
        if arr[i]=='-'or arr[i]=='+':
            maps[i//2+1][i//2+1]=cal(arr[i-1],arr[i],arr[i+1])
    for i in range(a-2,0,-1):
        x=1
        y=a-i
        cnt=1
        while i>=cnt:
            p=cal(arr[x*2-2],arr[x*2-1],maps[x+1][y])
            q=cal(maps[x][y-1],arr[y*2-1],arr[y*2])
            maps[x][y]=max(p,q)
            x+=1
            y+=1
            cnt+=1


    return maps[1][a-1]
a=['10' ,'-', '5', '+', '7', '+', '9', '-', '20', '-', '30', '+', '10']
solution(a)