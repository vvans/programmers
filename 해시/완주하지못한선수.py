
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i]!=completion[i]:
            return participant[i]
            break

    
    return participant[i+1]

a=["marina", "josipa", "nikola", "vinko", "filipa"]
b=["josipa", "filipa", "marina", "nikola"]
solution(a,b)
