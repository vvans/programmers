def solution(phone_book):
    answer = True
    a.sort()
    for i in range(0,len(phone_book)-1):
        k=phone_book[i]
        l=phone_book[i+1]
        if k == l[0:len(k)]:
            return False
    return answer

a=	["119", "97674223", "1195524421"]

print(solution(a))