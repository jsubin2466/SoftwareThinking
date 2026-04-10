n = int(input())
dic = {}
title=[]
for _ in range(n):
    title.append(input())
for i in title:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
maaax = max(dic.values())
first = []
for key, value in dic.items():
    if value == maaax:
        first.append(key)
print(min(first))
