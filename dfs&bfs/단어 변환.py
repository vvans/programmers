def solution(begin, target, words):
    # for i in words:
    def dfs(word,cnt,visit):
        global m
        if word==target:
            if m>cnt:
                m=cnt

        for k in range(len(words)):
            chk=0
            for i in range(len(word)):
                if words[k][i]!=word[i] and visit[k]==0:
                    chk+=1
            if chk==1:
                visit[k]=1
                dfs(words[k],cnt+1,visit)
                visit[k]=0

        return 0
    if target not in words:
        return 0
    global m
    m=100
    visit=[0 for i in range(len(words))]
    dfs(begin,0,visit)
    return m
a="hit"
b="cog"	
c=["hot", "dot", "dog", "lot", "log", "cog"]	
print(solution(a,b,c))