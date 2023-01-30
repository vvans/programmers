def solution(N, number):
    def search(a,b):
        l=[]
        for i in maps[a]:
            for j in maps[b]:
                if i!=0:
                    l.append(int(i/j))
                if j!=0:
                    l.append(int(j/i))
                l.append(int(i+j))
                l.append(int(i*j))
                l.append(int(i-j))
                l.append(int(j-i))
        return l
    maps=[]
    maps.append([0])
    maps.append([N])
    a=[1,N+N,N*N,10*N+N]
    maps.append(a)
    for i in range(7):
        maps.append([])
    pn=N*10+N
    for i in range(3,10):
        l=set()
        for j in range(1,i):
            for k in range(1,i):
                if j+k==i:
                    m=search(j,k)
                    for p in m:
                        l.add(p)
        for k in range(len(maps[i-1])):
            if maps[i-1][k]!= 0:
                l.add(int(maps[i-1][k]/N))
            l.add(int(N/maps[i-1][k]))
            l.add(int(maps[i-1][k]+N))
            l.add(int(maps[i-1][k]*N))
            l.add(int(maps[i-1][k]-N))
            l.add(int(N-maps[i-1][k]))
        l.add(pn*10+N)
        l=list(l)
        l.sort()
        for p in range(len(l)):
            if l[p]>0:
                break
        l=l[p:len(l)]

        maps[i]=l
    for i in range(1,10):
        if number in maps[i]:
            if i==9:
                return -1
            return i
    return -1

print(solution(8,53))