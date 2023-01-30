def solution(nums):
    nums.sort()
    count=1
    for i in range(0,len(nums)-1):
        if nums[i]!=nums[i+1]:
            count+=1
    
    if count>len(nums)/2:
        return int(len(nums)/2)
    return count

a=[3,3,3,2,2,2]	
print(solution(a))