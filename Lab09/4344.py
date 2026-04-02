c= int(input())
for i in range(c):
    li = list(map(int, input().split())) #표본생성

    summ = 0
    for j in range(1,li[0]+1): #평균생성
        summ += li[j]
    avg=summ/li[0]

    count = 0
    for k in range(1, li[0]+1):
        if li[k]>avg:
            count += 1
    pct = count/li[0]*100
    print(f"{pct:.3f}")
