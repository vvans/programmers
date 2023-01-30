from heapq import heappop, heappush
def solution(scoville, K):
    heap=[]
    for i in scoville:
        heappush(heap,i)
    answer=0
    while True:
        a=heappop(heap)
        if a>=K:
            break
        if len(heap)==0:
            return -1
        b=heappop(heap)
        c=a+(b*2)
        heappush(heap,c)
        answer+=1
    return answer

a=[1, 1]	
print(solution(a,7))