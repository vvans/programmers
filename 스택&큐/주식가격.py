def solution(prices):
    answer = [0 for i in range(len(prices))]
    for i in range(len(prices)-1):
        for j in range(i+1,len(prices)):
            if prices[i]<=prices[j]:
                answer[i]+=1
            else:
                answer[i]+=1
                break
    return answer
a=[1, 2, 3, 2, 3]
print(solution(a))