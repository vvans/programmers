def solution(numbers, target):
    global answer
    answer = 0
    def num(depth,s,target):
        if depth==len(numbers):
            if s==target:
                global answer
                answer+=1
        else:
            num(depth+1,s+numbers[depth],target)
            num(depth+1,s-numbers[depth],target)
    num(0,0,target)
    return answer
a=[4, 1, 2, 1]	
b=4
print(solution(a,b))