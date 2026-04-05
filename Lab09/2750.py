n = int(input())
li = list(int(input()) for _ in range(n))
sort_li=sorted(li)
for i in range(n):
    print(sort_li[i])
