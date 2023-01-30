def solution(genres, plays):
    class gen:
        def __init__(self,g):
            self.gen=g
            self.s=0
            self.idx=[]
        def idxd(self,ind,pl):
            self.idx.append([pl,ind])
        def sum(self,hap):
            self.s+=hap
    answer=[]
    play={}
    lis=[]
    s=[]
    for i in range(len(genres)):
        if genres[i] not in play:
            play[genres[i]]=gen(genres[i])
            lis.append(genres[i])
            s.append(0)
        s[lis.index(genres[i])]+=plays[i]
        play[genres[i]].sum(plays[i])
        play[genres[i]].idxd(i,plays[i])
    s.sort(reverse=True)
    for i in s:
        for j in lis:
            if play[j].s==i:
                play[j].idx.sort(key=lambda x: -x[0])
                if len(play[j].idx)==1:
                    answer.append(play[j].idx[0][1])
                else:
                    for k in range(2):
                        answer.append(play[j].idx[k][1])

    return answer

a=["classic", "pop", "classic", "classic", "pop"]	
b=[500, 600, 500, 500, 2500]
print(solution(a,b))