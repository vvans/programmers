def solution(arr):
    answer = []
    for i in range(0,len(arr)-1):
        if arr[i]!=arr[i+1]:
            answer.append(arr[i])
    answer.append(arr[i+1])
    print('Hello Python')
    return answer

a=[1,1,3,3,0,1,1]
print(solution(a))