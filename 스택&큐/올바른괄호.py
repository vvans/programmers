def solution(s):
    answer = True
    cnt=0
    for i in s:
        if i=='(':
            cnt+=1
        else:
            cnt-=1
        if cnt<0:
            return False
    
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    if cnt!=0:
        return False
    print('Hello Python')

    return True
a="() )( ()"
print(solution(a))