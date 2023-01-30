def solution(bridge_length, weight, truck_weights):
    re=weight
    index=0
    t_index=0
    ti=0
    watch=[0 for i in range(len(truck_weights))]
    while True:
        if t_index<len(truck_weights) and truck_weights[t_index]<=re:
            re-=truck_weights[t_index]
            t_index+=1
        for i in range(t_index):
            watch[i]+=1
        if watch[index]==bridge_length:
            re+=truck_weights[index]
            index+=1
            if index==len(truck_weights):
                return watch[0]+1




a=100
b=100
c=[10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
print(solution(a,b,c))