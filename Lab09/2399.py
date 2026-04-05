n=int(input())
li=list(map(int, input().split()))

count = 0
for i in range(n):
    for j in range(n):
        count += abs(li[i]-li[j])
print(count)

