import sys
input = sys.stdin.readline

k, l = map(int, input().split())
stdic={}
for _ in range(l):
    student = input().strip()
    if student in stdic:
        del stdic[student]
        stdic[student]=1
    else:
        stdic[student]=1

count = 0
for i in stdic:
    if count == k:
        break
    print(i)
    count+=1
